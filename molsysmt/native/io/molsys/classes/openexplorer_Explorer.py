def from_openexplorer_Explorer (item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native.molsys import MolSys
    from molsysmt.native.io.topology.classes import from_openexplorer_Explorer as openexplorer_Explorer_to_molsysmt_Topology
    from molsysmt.native.io.trajectory.classes import from_openexplorer_Explorer as openexplorer_Explorer_to_molsysmt_Trajectory

    tmp_item = MolSys()
    tmp_item.topology, _ = openexplorer_Explorer_to_molsysmt_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory, _ = openexplorer_Explorer_to_molsysmt_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

