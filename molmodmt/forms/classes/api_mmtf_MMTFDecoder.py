from os.path import basename as _basename
from mmtf import MMTFDecoder as _mmtf_MMTFDecoder

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _mmtf_MMTFDecoder : form_name,
    'mmtf.MMTFDecoder' : form_name
}


def to_mmtf(item, output_file_path=None, atom_indices=None, frame_indices=None):

    from mmtf.api.default_api import write_mmtf, MMTFDecoder
    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return write_mmtf(output_file_path, tmp_item, MMTFDecoder.pass_data_on)

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError

###### Get

## atom

## system

def get_n_atoms_from_system (item, indices=None, frame_indices=None):

    return item.num_atoms

def get_n_frames_from_system(item, indices=None, frame_indices=None):

    return item.num_models

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)
