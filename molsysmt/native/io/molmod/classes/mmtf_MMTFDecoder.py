
def from_mmtf_MMTFDecoder(item, atom_indices='all', frame_indices='all'):

    from molsysmt.native.molsys import MolSys
    from molsysmt.native.io.card import from_mmtf_MMTFDecoder as to_card
    from molsysmt.native.io.composition import from_mmtf_MMTFDecoder as to_composition
    from molsysmt.native.io.trajectory import from_mmtf_MMTFDecoder as to_trajectory

    tmp_item = MolSys()
    tmp_item.composition = to_composition(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = to_trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.card = None
    tmp_item.topography = None
    return tmp_item
