import numpy as np
from .exceptions import *

def one_system(molecular_system=None, selection=None, frame_indices=None, form=None, syntaxis='MolSysMT'):

    from molsysmt.multitool import convert, select

    atom_indices=None

    if form is not None:
        tmp_molecular_system=convert(molecular_system, form)
    else:
        tmp_molecular_system=item

    if selection is not None:
        atom_indices=select(molecular_system, selection, syntaxis=syntaxis)

    frame_indices=frameslist(tmp_molecular_system, frame_indices)

    return tmp_molecular_system, atom_indices, frame_indices

def frameslist(molecular_system=None, frame_indices=None):

    from molsysmt.multitool import get

    if frame_indices is None:
        frame_indices = list(np.arange(get(molecular_system, n_frames=True), dtype=int))
    elif type(frame_indices) == int:
        frame_indices = np.asarray([frame_indices])
    elif type(frame_indices) == list:
        frame_indices = np.asarray(frame_indices)
    elif type(frame_indices) == np.ndarray:
        frame_indices = frame_indices
    elif frame == 'all':
        frame_indices = np.arange(get(molecular_system, n_frames=True))

    return frame_indices

def coordinates(molecular_system=None, atom_indices=None, frame_indices=None, form='molsysmt.MolSys'):

    if form=='molsysmt.MolSys':
        tmp_molecular_system = molecular_system.trajectory
    elif form=='molsysmt.Trajectory':
        tmp_molecular_system = molecular_system
    else:
        raise NotImplementedError()

    if atom_indices is not None:
        if frame_indices is not None:
            tmp_coordinates = tmp_molecular_system.coordinates[frame_indices,:,:]
            tmp_coordinates = tmp_coordinates[:,atom_indices,:]
        else:
            tmp_coordinates = tmp_item.coordinates[:,atom_indices,:]
    else:
        if frame_indices is not None:
            tmp_frame_indices=frameslist(tmp_molecular_system, frame_indices)
            tmp_coordinates = tmp_item.coordinates[frame_indices,:,:]
        else:
            tmp_coordinates = tmp_item.coordinates

    tmp_natoms = tmp_coordinates.shape[1]
    tmp_nframes = tmp_coordinates.shape[0]

    if tmp_natoms==1 and tmp_nframes==1:
        tmp_coordinates = tmp_coordinates.reshape(1,1,3)
    elif tmp_natoms==1:
        tmp_coordinates = tmp_coordinates.reshape(tmp_nframes,1,3)
    elif tmp_nframes==1:
        tmp_coordinates = tmp_coordinates.reshape(1,tmp_natoms,3)

    return tmp_coordinates, tmp_nframes, tmp_natoms


def comparison_two_systems(molecular_system_1=None, selection_1=None, frame_indices_1=None,
                           molecular_system_2=None, selection_2=None, frame_indices_2=None,
                           form=None, syntaxis='MolSysMT'):

    from molsysmt.multitool import convert, select

    single_molecular_system = False
    diff_selection = True
    atom_indices_1 = None
    atom_indices_2 = None

    if molecular_system1 is None and molecular_system_2 is None:
        raise BadCallError(BadCallMessage)

    if molecular_system_1 is None or molecular_system_2 is None:
        single_molecular_system = True
        if molecular_system_1 is None:
            molecular_system_1 = molecular_system_2
        else:
            molecular_system_2 = molecular_system_1

    if form is not None:
        tmp_molecular_system_1=convert(molecular_system_1, form)
        tmp_molecular_system_2=convert(molecular_system_2, form)
    else:
        tmp_molecular_system_1=molecular_system_1
        tmp_molecular_system_2=molecular_system_2

    if selection_1 is not None:
        atom_indices_1 = select(tmp_molecular_system_1, selection_1, syntaxis=syntaxis)

    if selection_2 is not None:
        atom_indices_2 = select(tmp_molecular_system_2, selection_2, syntaxis=syntaxis)

    if selection_1 is None and selection_2 is None:

        atom_indices_1= None
        atom_indices_2= None

    elif selection_1 is None or selection_2 is None:
        if single_molecular_system is True:
            diff_selection = False
            if selection_1 is None:
                atom_indices_1 = atom_indices_2
            else:
                atom_indices_2 = atom_indices_1
        else:
            if selection_1 is None:
                atom_indices_1 = select(tmp_molecular_system_1, selection_2, syntaxis=syntaxis)
            else:
                atom_indices_2 = select(tmp_molecular_system_2, selection_1, syntaxis=syntaxis)

    frame_indices_1 = frameslist(tmp_molecular_system_1, frame_indices_1)
    frame_indices_2 = frameslist(tmp_molecular_system_2, frame_indices_2)

    return tmp_molecular_system_1, atom_indices_1, frame_indices_1, \
           tmp_molecular_system_2, atom_indices_2, frame_indices_2, \
           single_molecular_system, diff_selection

