import numpy as np
from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import pyunitwizard as puw
from molsysmt.molecular_system import molecular_system_components

form_name='XYZ'

is_form={
}

info=["",""]

has = molecular_system_components.copy()
for ii in ['coordinates']:
    has[ii]=True

def item_in_good_shape(item):

    unit = puw.get_unit(item)
    value = puw.get_value(item)

    if type(value)==list:
        value = np.array(value)

    if len(value.shape)==2:
        value = np.expand_dims(value, axis=0)

    return value*unit

def this_Quantity_has_XYZ_shape(item):

    # Only np.arrays of shape [n_frames, n_particles, coordinates] or [n_particles, coordinates] are
    # admitted

    has_right_shape = False

    shape = np.shape(item)

    if len(shape)==3 and shape[-1]==3:
        has_right_shape = True
    elif len(shape)==2 and shape[-1]==3:
        has_right_shape = True

    return has_right_shape

def this_Quantity_is_XYZ(item):

    # Only np.arrays of shape [n_frames, n_particles, coordinates] or [n_particles, coordinates] are
    # admitted

    is_length = puw.compatibility(item, puw.unit('nm'))
    has_right_shape = this_Quantity_has_XYZ_shape(item)

    return (has_right_shape and is_length)

def to_molsysmt_Trajectory(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native.io.trajectory.classes import from_XYZ as XYZ_to_molsysmt_Trajectory

    tmp_item, tmp_molecular_system = XYZ_to_molsysmt_Trajectory(item,
            molecular_system=molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def to_xyznpy(item, molecular_system=None, atom_indices='all', frame_indices='all', output_filename=None):

    comment = None
    atom_names = None
    xyz = None
    unit_name = None

    xyz = item._value
    unit_name = item.unit.get_name()

    with open(output_filename, 'wb') as fff:
        np.save(fff, comment)
        np.save(fff, atom_names)
        np.save(fff, unit_name)
        np.save(fff, xyz)

    tmp_item = output_filename
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_XYZ(item, molecular_system=None, atom_indices='all', frame_indices='all', copy_if_all=True):

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
        from copy import copy
        tmp_item = copy(item)
    else:
        tmp_item = get_coordinates_from_atom(item, indices=atom_indices, frame_indices=frame_indices)

    return tmp_item

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

###### Get

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    tmp_item = item_in_good_shape(item)
    tmp_coordinates=tmp_item[:,:,:]

    if indices is not 'all':
        tmp_coordinates = tmp_item[:,indices,:]

    if frame_indices is not 'all':
        tmp_coordinates = tmp_coordinates[frame_indices,:,:]

    return tmp_coordinates


## group

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## component

def get_component_id_from_component (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_component_name_from_component (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_component_type_from_component (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## molecule

def get_molecule_id_from_molecule (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## chain

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## entity

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    tmp_item = item_in_good_shape(item)
    return tmp_item.shape[1]

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    tmp_item = item_in_good_shape(item)
    tmp_coordinates=tmp_item[:,:,:]
    if frame_indices is not 'all':
        tmp_coordinates = tmp_coordinates[frame_indices,:,:]

    return tmp_coordinates

def get_box_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_time_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_step_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    tmp_item = item_in_good_shape(item)
    return tmp_item.shape[0]

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

## bond

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    raise NotWithThisFormError()



