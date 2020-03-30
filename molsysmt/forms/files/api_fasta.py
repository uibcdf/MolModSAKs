from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'fasta': form_name,
    'FASTA': form_name
    }

info=["",""]

def to_biopython_SeqRecord(item, atom_indices='all', frame_indices='all'):

    from Bio.SeqIO import read as Bio_SeqRecord_reader
    from molsysmt.forms.classes.api_Bio_SeqRecord import extract_subsystem as extract_Bio_SeqRecord
    tmp_item=Bio_SeqRecord_reader(item,'fasta')
    tmp_item=extract_Bio_SeqRecord(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def extract_subsystem(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError


###### Get

## system

def get_form_from_system(item, indices='all', frame_indices='all'):

    from molsysmt import get_form
    return get_form(item)
