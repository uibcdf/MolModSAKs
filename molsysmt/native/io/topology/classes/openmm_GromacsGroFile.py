def from_openmm_GromacsGroFile(item, molecular_system, atom_indices='all', frame_indices='all'):

    from molsysmt.forms.classes.api_openmm_GromacsGroFile import to_openmm_Topology as openmm_GromacsGroFile_to_openmm_Topology
    from .openmm_Topology import from_openmm_Topology as openmm_Topology_to_molsysmt_Topology

    tmp_item, tmp_molecular_system = openmm_GromacsGroFile_to_openmm_Topology(item, molecular_system)
    tmp_item, tmp_molecular_system = openmm_Topology_to_molsysmt_Topology(tmp_item, tmp_molecular_system)

    return tmp_item, tmp_molecular_system

