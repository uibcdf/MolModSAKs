from os.path import basename as _basename
from simtk.openmm import Context as _openmm_Context

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _openmm_Context : form_name,
    'openmm.Context' : form_name
}

info=["",""]
with_topology=True
with_trajectory=True

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

###### Get

def get_n_atoms_from_atom(item, indices='all', frame_indices='all'):

    if indices is 'all':
        return item.getSystem().getNumParticles()
    else:
        len(indices)

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    from numpy import array as _array

    coordinates = item.getState(getPositions=True).getPositions(asNumpy=True)
    units = coordinates.unit
    coordinates = coordinates.reshape([1, coordinates.shape[0], coordinates.shape[1]])

    if frame_indices is not 'all':
        coordinates = coordinates[frame_indices,:,:]

    if indices is not 'all':
        coordinates = coordinates[:,indices,:]

    coordinates = coordinates * units

    return coordinates


def get_form_from_atom(item, indices='all', frame_indices='all'):

    return form_name

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    return item.getSystem().getNumParticles()

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    from numpy import array as _array

    coordinates = item.getState(getPositions=True).getPositions(asNumpy=True)
    units = coordinates.unit
    coordinates = coordinates.reshape([1, coordinates.shape[0], coordinates.shape[1]])

    if frame_indices is not 'all':
        coordinates = coordinates[frame_indices,:,:]

    coordinates = coordinates * units

    return coordinates

def get_box_from_system(item, indices='all', frame_indices='all'):

    box = item.getState().getPeriodicBoxVectors(asNumpy=True)
    units = box.unit
    box = box.reshape([1, box.shape[0], box.shape[1]])

    if frame_indices is not 'all':
        box = box[frame_indices,:,:]

    box = box * units

    return box

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    from molsysmt import box_shape_from_box_vectors
    box = get_box_from_system(item, indices=indices, frame_indices=frame_indices)
    return box_shape_from_box_vectors(box)

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    from molsysmt import box_lengths_from_box_vectors
    box = get_box_from_system(item, indices=indices, frame_indices=frame_indices)
    return box_lengths_from_box_vectors(box)

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    from molsysmt import box_angles_from_box_vectors
    box = get_box_from_system(item, indices=indices, frame_indices=frame_indices)
    return box_angles_from_box_vectors(box)

def get_time_from_system(item, indices='all', frame_indices='all'):

    time = item.getState().getTime()
    return time

def get_step_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    return item.setPositions(value[0])

