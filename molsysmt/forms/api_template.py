from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import numpy as np
from molsysmt import MolSys as _molsysmt_MolSys
from molsysmt import puw
from molsysmt.molecular_system import molecular_system_components

form_name='molsysmt.MolSys'

is_form={
    _molsysmt_MolSys : form_name,
    'molsysmt.MolSys': form_name
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'bonds', 'coordinates', 'box']:
    has[ii]=True

def to_molsysmt_MolSys(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def to_molsysmt_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def to_molsysmt_Trajectory(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def to_nglview_NGLView(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def to_template_form(item, molecular_system=None, atom_indices='all', frame_indices='all', copy_if_all=True):

    tmp_molecular_system = None

    if (atom_indices is 'all') and (frame_indices is 'all'):
        if copy_if_all:
            tmp_item = extract_item(item)
            if molecular_system is not None:
                tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
        else:
            tmp_item = item
            if molecular_system is not None:
                tmp_molecular_system = molecular_system
    else:
        tmp_item = extract_item(item, atom_indices=atom_indices, frame_indices=frame_indices)
        if molecular_system is not None:
            tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def extract_item(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        tmp_item = item.copy()
    else:
        raise NotImplementedError()

    return tmp_item

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

###### Get

## atom

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_index_from_atom as _get
    return _get(item, indices=indices)

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_index_from_atom as _get
    return _get(item, indices=indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError()

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    tmp_step = get_step_from_system(item, frame_indices=frame_indices)
    tmp_time = get_time_from_system(item, frame_indices=frame_indices)
    tmp_box = get_box_from_system(item, frame_indices=frame_indices)
    tmp_coordinates = get_coordinates_from_atom(item, indices=indices, frame_indices=frame_indices)

    return tmp_step, tmp_time, tmp_coordinates, tmp_box

## group

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

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

    from molsysmt.elements.molecule import get_molecule_id_from_molecule as get
    return get(item, indices)

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_name_from_molecule as get
    return get(item, indices)

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_type_from_molecule as get
    return get(item, indices)

## chain

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError()

## entity

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_id_from_molecule as get
    return get(item, indices)

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_name_from_molecule as get
    return get(item, indices)

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_type_from_molecule as get
    return get(item, indices)

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_n_components_from_system as get
    return get(item, indices)

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_n_molecules_from_system as get
    return get(item, indices)

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_n_entities_from_system as get
    return get(item, indices)

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_box_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_box_volume_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_time_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_step_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

## bond

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError()

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError()

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError()

