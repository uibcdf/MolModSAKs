import numpy as np
from molsysmt import puw
from molsysmt._private_tools.molecular_system import digest_molecular_system
from molsysmt._private_tools.frame_indices import digest_frame_indices
from .lib import geometry as libgeometry

def get_dihedral_angles(molecular_system, dihedral_angle=None, selection='all', quartets=None,
                        frame_indices='all', syntaxis='MolSysMT', pbc=False):

    from molsysmt.multitool import get

    molecular_system = digest_molecular_system(molecular_system)
    frame_indices = digest_frame_indices(frame_indices)

    if quartets is None:

        from molsysmt import covalent_dihedral_quartets

        quartets = covalent_dihedral_quartets(molecular_system, dihedral_angle=dihedral_angle, selection=selection, syntaxis=syntaxis)

    elif type(quartets) in [list,tuple]:
        quartets = np.array(quartets, dtype=int)
    elif type(quartets) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = quartets.shape

    if len(shape)==1:
        if shape[0]==4:
            quartets=quartets.reshape([1,4])
        else:
            raise ValueError
    elif len(shape)==2:
        if shape[1]!=4:
            raise ValueError
    else:
        raise ValueError


    coordinates = get(molecular_system, target='system', frame_indices=frame_indices, coordinates=True)

    n_angles = quartets.shape[0]
    n_frames = coordinates.shape[0]
    n_atoms = coordinates.shape[1]

    if pbc:

        box, box_shape = get(molecular_system, target='system', frame_indices=frame_indices, coordinates=True, box=True, box_shape=True)
        if box_shape is None:
            raise ValueError("The system has no PBC box. The input argument 'pbc' can not be True.")
        orthogonal = 0

        if box_shape is None:
            orthogonal =1
        elif box_shape == 'cubic':
            orthogonal =1

    else:

        orthogonal = 1
        box = np.zeros([n_frames,3,3])*puw.unit('nm')

    box = np.asfortranarray(puw.get_value(box, to_unit='nm'), dtype='float64')
    coordinates = np.asfortranarray(puw.get_value(coordinates, to_unit='nm'), dtype='float64')

    angles = libgeometry.dihedral_angles(coordinates, box, orthogonal, int(pbc), quartets, n_angles, n_atoms, n_frames)
    angles = np.ascontiguousarray(angles)*puw.unit('degrees')

    return angles

def ramachandran_angles(molecular_system, selection='all', frame_indices='all', syntaxis='MolSysMT', pbc=False, plot=False):

    from molsysmt.covalent import covalent_dihedral_quartets

    molecular_system = digest_molecular_system(molecular_system)
    frame_indices = digest_frame_indices(frame_indices)

    phi_covalent_chain = covalent_dihedral_quartets(molecular_system, dihedral_angle='phi', selection=selection, syntaxis=syntaxis)
    psi_covalent_chain = covalent_dihedral_quartets(molecular_system, dihedral_angle='psi', selection=selection, syntaxis=syntaxis)

    n_chains = phi_covalent_chain.shape[0]

    angles = get_dihedral_angles(molecular_system, quartets=np.vstack([phi_covalent_chain, psi_covalent_chain]), frame_indices=frame_indices, pbc=pbc)

    return phi_covalent_chain, psi_covalent_chain, angles[:,:n_chains], angles[:,n_chains:]

def shift_dihedral_angles(molecular_system, quartets=None, angles_shifts=None, blocks=None,
                          frame_indices='all', pbc=False, in_place=True, engine='MolSysMT'):

    from molsysmt.multitool import get

    molecular_system = digest_molecular_system(molecular_system)
    frame_indices = digest_frame_indices(frame_indices)

    if type(quartets) in [list,tuple]:
        quartets = np.array(quartets, dtype=int)
    elif type(quartets) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = quartets.shape

    if len(shape)==1:
        if shape[0]==4:
            quartets=quartets.reshape([1,4])
        else:
            raise ValueError
    elif len(shape)==2:
        if shape[1]!=4:
            raise ValueError
    else:
        raise ValueError

    n_quartets = quartets.shape[0]
    n_frames = get(molecular_system, target='system', frame_indices=frame_indices, n_frames=True)

    angles_shifts_units = puw.get_unit(angles_shifts)
    angles_shifts_value = puw.get_value(angles_shifts)

    if type(angles_shifts_value) in [float]:
        if (n_quartets==1 and n_frames==1):
            angles_shifts_value = np.array([[angles_shifts_value]], dtype=float)
        else:
            raise ValueError("angles_shifts do not match the number of frames and quartets")
    elif type(angles_shifts_value) in [list,tuple]:
        angles_shifts_value = np.array(angles_shifts_value, dtype=float)
    elif type(angles_shifts_value) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = angles_shifts_value.shape

    if len(shape)==1:
        angles_shifts_value = angles_shifts_value.reshape([n_frames, n_quartets])

    angles_shifts=angles_shifts_value*angles_shifts_units

    angles = get_dihedral_angles(molecular_system, quartets=quartets, frame_indices=frame_indices, pbc=pbc)
    angles = angles + angles_shifts

    return set_dihedral_angles(molecular_system, quartets=quartets, angles=angles, blocks=None,
                               frame_indices=frame_indices, pbc=pbc, in_place=in_place, engine=engine)

def set_dihedral_angles(molecular_system, quartets=None, angles=None, blocks=None, frame_indices='all', pbc=False,
                        in_place=True, engine='MolSysMT'):

    from molsysmt.multitool import get, convert, set, copy

    molecular_system = digest_molecular_system(molecular_system)
    frame_indices = digest_frame_indices(frame_indices)

    if type(quartets) in [list,tuple]:
        quartets = np.array(quartets, dtype=int)
    elif type(quartets) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = quartets.shape

    if len(shape)==1:
        if shape[0]==4:
            quartets=quartets.reshape([1,4])
        else:
            raise ValueError
    elif len(shape)==2:
        if shape[1]!=4:
            raise ValueError
    else:
        raise ValueError

    n_atoms = get(molecular_system, target='system', n_atoms=True)
    n_quartets = quartets.shape[0]
    n_frames = get(molecular_system, target='system', frame_indices=frame_indices, n_frames=True)

    angles_units = puw.get_unit(angles)
    angles_value = puw.get_value(angles)

    if type(angles_value) in [float]:
        if (n_quartets==1 and n_frames==1):
            angles_value = np.array([[angles_value]], dtype=float)
        else:
            raise ValueError("angles do not match the number of frames and quartets")
    elif type(angles_value) in [list,tuple]:
        angles_value = np.array(angles_value, dtype=float)
    elif type(angles_value) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = angles_value.shape

    if len(shape)==1:
        angles_value = angles_value.reshape([n_frames, n_quartets])

    angles = angles_value*angles_units

    if engine=='MolSysMT':

        if blocks is None:

            from molsysmt.covalent import covalent_blocks

            blocks = []

            for quartet in quartets:

                tmp_blocks = covalent_blocks(molecular_system, remove_bonds=[quartet[1], quartet[2]])
                blocks.append(tmp_blocks)


        coordinates = get(molecular_system, target='system', frame_indices=frame_indices, coordinates=True)

        if pbc:

            box, box_shape = get(molecular_system, target='system', frame_indices=frame_indices, coordinates=True, box=True, box_shape=True)
            if box_shape is None:
                raise ValueError("The system has no PBC box. The input argument 'pbc' can not be True.")
            orthogonal = 0

            if box_shape is None:
                orthogonal =1
            elif box_shape == 'cubic':
                orthogonal =1

        else:

            orthogonal = 1
            box= np.zeros([n_frames,3,3])*puw.unit('nm')

        length_units = puw.unit(coordinates)
        box = np.asfortranarray(puw.get_value(box, to_unit=length_units), dtype='float64')
        coordinates = np.asfortranarray(puw.get_value(coordinates), dtype='float64')
        angles = np.asfortranarray(puw.get_value(angles), dtype='float64')

        aux_blocks = []
        aux_atoms_per_block = []

        for block in blocks:

            aux_atoms_per_block.append(len(block[1]))
            aux_blocks.append(list(block[1]))

        aux_blocks = np.ravel(aux_blocks)
        aux_atoms_per_block = np.array(aux_atoms_per_block, dtype=int)

        libgeometry.set_dihedral_angles(coordinates, box, orthogonal, int(pbc), quartets, angles,
                                         aux_blocks, aux_atoms_per_block, n_quartets, n_atoms, n_frames, aux_blocks.shape[0])

        coordinates=np.ascontiguousarray(coordinates)*length_units

        if in_place:
            return set(molecular_system, target='system', coordinates=coordinates, frame_indices=frame_indices)
        else:
            tmp_molecular_system = copy(molecular_system)
            set(tmp_molecular_system, target='system', coordinates=coordinates, frame_indices=frame_indices)
            return tmp_molecular_system

    else:

        raise NotImplementedError

