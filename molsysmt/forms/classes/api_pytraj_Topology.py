from molsysmt._private_tools.exceptions import *
import numpy as np
from molsysmt.forms.common_gets import *
from pytraj import Topology as _pytraj_Topology
from molsysmt.molecular_system import molecular_system_components

form_name='pytraj.Topology'

is_form={
    _pytraj_Topology : form_name,
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'bonds']:
    has[ii]=True

def to_molsysmt_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native.io.topology.classes import from_pytraj_Topology as pytraj_Topology_to_molsysmt_Topology
    from molsysmt.forms.classes.api_molsysmt_Topology import to_molsysmt_Topology as molsysmt_Topology_to_molsysmt_Topology

    tmp_item, tmp_molecular_system = pytraj_Topology_to_molsysmt_Topology(item, molecular_system=molecular_system)
    tmp_item, tmp_molecular_system = molsysmt_Topology_to_molsysmt_Topology(tmp_item,
            molecular_system=tmp_molecular_system, atom_indices=atom_indices, copy_if_all=False)

    return tmp_item, tmp_molecular_system

def to_pytraj_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all', copy_if_all=True):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        raise NotImplementedError()
    else:
        raise NotImplementedError()

def extract_item(item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

###### Get

## atom

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [None for atom in item.atoms]
    else:
        output = [None for ii in indices]
    output = np.array(output)
    return output

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [atom.name for atom in item.atoms]
    else:
        output = [item.atom(ii).name for ii in indices]
    output = np.array(output, dtype=object)
    return output

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [atom.type for atom in item.atoms]
    else:
        output = [item.atom(ii).type for ii in indices]
    output = np.array(output, dtype=object)
    return output

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [atom.resid for atom in item.atoms]
    else:
        output = [item.atom(ii).resid for ii in indices]
    output = np.array(output)
    return output

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [atom.chain for atom in item.atoms]
    else:
        output = [item.atom(ii).chain for ii in indices]
    output = np.array(output)
    return output

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        output = [atom.molnum for atom in item.atoms]
    else:
        output = [item.atom(ii).molnum for ii in indices]
    output = np.array(output)
    return output

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bond_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_bonds_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        return get_n_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_inner_bond_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## group

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## component

def get_component_id_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_id_from_component as get
    return get(item, indices)

def get_component_name_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_name_from_component as get
    return get(item, indices)

def get_component_type_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_type_from_component as get
    return get(item, indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    raise NotImplementedError

## chain

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

## entity

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    raise NotImplementedError

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    return item.n_atoms

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    return item.n_residues

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    output = get_component_index_from_atom(item, indices='all')
    output = np.unique(output)
    return output.shape[0]

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    try:
        n_bonds = item.bond_indices.shape[0]
    except:
        n_bonds = 0

    return n_bonds

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_time_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_step_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## bond

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    output = None

    if indices is 'all':
        output = item.bond_indices
    else:
        output = item.bond_indices[indices]

    return output

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

