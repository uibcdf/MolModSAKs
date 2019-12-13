class Composition():

    def __init__(self):

        self.bioassembly = None

        self.entity = []
        self.entity_indices = []
        self.n_entities = 0

        self.molecule = []
        self.molecule_indices = []
        self.n_molecules = 0

        self.chain = []
        self.chain_indices = []
        self.n_chains = 0

        self.component = []
        self.component_indices = []
        self.n_components = 0

        self.group = []
        self.group_indices = []
        self.n_groups = 0

        self.atom = []
        self.atom_indices = []
        self.n_atoms = 0

        self.bond = []
        self.bond_indices = []
        self.bonded_atom_indices = []
        self.n_bonds = 0

        self.dataframe = None

    def _update_elements_from_bioassembly(self):

        if self.bioassembly is not None:

            self.entity = self.bioassembly.entity
            self.entity_indices = self.bioassembly.entity_indices
            self.n_entities = self.bioassembly.n_entities

            self.molecule = self.bioassembly.molecule
            self.molecule_indices = self.bioassembly.molecule_indices
            self.n_molecules = self.bioassembly.n_molecules

            self.chain = self.bioassembly.chain
            self.chain_indices = self.bioassembly.chain_indices
            self.n_chains = self.bioassembly.n_chains

            self.component = self.bioassembly.component
            self.component_indices = self.bioassembly.component_indices
            self.n_components = self.bioassembly.n_components

            self.group = self.bioassembly.group
            self.groups = self.bioassembly.group_indices
            self.n_groups = self.bioassembly.n_groups

            self.atom = self.bioassembly.atom
            self.atom_indices = self.bioassembly.atom_indices
            self.n_atoms = self.bioassembly.n_atoms

            self.bond = self.bioassembly.bond
            self.bond_indices = self.bioassembly.bond_indices
            self.bonded_atom_indices = self.bioassembly.bonded_atom_indices
            self.n_bonds = self.bioassembly.n_bonds

    def _build_from_dataframe(self, dataframe):

        from molmodmt.native import elements

        current_atom = None
        current_atom_index = 0
        last_atom_dataframe_index = -1

        current_group = None
        current_group_index = 0
        last_group_dataframe_index = -1

        current_component = None
        current_component_index = 0
        last_component_dataframe_index = -1

        current_chain = None
        current_chain_index = 0
        last_chain_dataframe_index = -1

        current_molecule = None
        current_molecule_index = 0
        last_molecule_dataframe_index = -1

        current_entity = None
        current_entity_index = 0
        last_entity_dataframe_index = -1

        current_bioassembly = None
        current_bioassembly_index = 0
        last_bioassembly_dataframe_index = -1


        for row_index, row in dataframe.iterrows():

            if last_atom_dataframe_index!=row['atom.index']:
                current_atom = elements.Atom(index=current_atom_index, id=row['atom.id'], name=row['atom.name'], type=row['atom.type'])
                self.atom.append(current_atom)
                current_atom_index += 1
                last_atom_dataframe_index = row['atom.index']

            if last_group_dataframe_index!=row['group.index']:
                current_group = elements.group_initialization_wizard((index=current_group_index,
                    id=row['group.id'], name=row['group.name'], type=row['group.type'])
                self.group.append(current_group)
                current_group_index += 1
                last_group_dataframe_index = row['group.index']

            if last_component_dataframe_index!=row['component.index']:
                current_component = elements.Component((index=current_component_index,
                    id=row['component.id'], name=row['component.name'], type=row['component.type'])
                self.component.append(current_component)
                current_component_index += 1
                last_component_dataframe_index = row['component.index']

            if last_chain_dataframe_index!=row['chain.index']:
                current_chain = elements.Chain((index=current_chain_index,
                    id=row['chain.id'], name=row['chain.name'], type=row['chain.type'])
                self.chain.append(current_chain)
                current_chain_index += 1
                last_chain_dataframe_index = row['chain.index']

            if last_molecule_dataframe_index!=row['molecule.index']:
                current_molecule = elements.molecule_intialization_wizard((index=current_molecule_index,
                    id=row['molecule.id'], name=row['molecule.name'], type=row['molecule.type'])
                self.molecule.append(current_molecule)
                current_molecule_index += 1
                last_molecule_dataframe_index = row['molecule.index']








        pass

    def _update_dataframe(self):

        from molmodmt.native import DataFrame
        from pandas import Series

        tmp_item = DataFrame()

        tmp_item['atom.index'] = Series(atom.index for atom in self.atom).values
        tmp_item['atom.name'] = Series(atom.name for atom in self.atom).values
        tmp_item['atom.id'] = Series(atom.id for atom in self.atom).values
        tmp_item['atom.type'] = Series(atom.type for atom in self.atom).values

        tmp_item['group.index'] = Series(atom.group.index for atom in self.atom).values
        tmp_item['group.name'] = Series(atom.group.name for atom in self.atom).values
        tmp_item['group.id'] = Series(atom.group.id for atom in self.atom).values
        tmp_item['group.type'] = Series(atom.group.type for atom in self.atom).values

        tmp_item['component.index'] = Series(atom.component.index for atom in self.atom).values
        tmp_item['component.name'] = Series(atom.component.name for atom in self.atom).values
        tmp_item['component.id'] = Series(atom.component.id for atom in self.atom).values
        tmp_item['component.type'] = Series(atom.component.type for atom in self.atom).values

        tmp_item['chain.index'] = Series(atom.chain.index for atom in self.atom).values
        tmp_item['chain.name'] = Series(atom.chain.name for atom in self.atom).values
        tmp_item['chain.id'] = Series(atom.chain.id for atom in self.atom).values
        tmp_item['chain.type'] = Series(atom.chain.type for atom in self.atom).values

        tmp_item['molecule.index'] = Series(atom.molecule.index for atom in self.atom).values
        tmp_item['molecule.name'] = Series(atom.molecule.name for atom in self.atom).values
        tmp_item['molecule.id'] = Series(atom.molecule.id for atom in self.atom).values
        tmp_item['molecule.type'] = Series(atom.molecule.type for atom in self.atom).values

        tmp_item['entity.index'] = Series(atom.entity.index for atom in self.atom).values
        tmp_item['entity.name'] = Series(atom.entity.name for atom in self.atom).values
        tmp_item['entity.id'] = Series(atom.entity.id for atom in self.atom).values
        tmp_item['entity.type'] = Series(atom.entity.type for atom in self.atom).values

        tmp_item['bioassembly.index'] = Series(atom.bioassembly.index for atom in self.atom).values
        tmp_item['bioassembly.name'] = Series(atom.bioassembly.name for atom in self.atom).values
        tmp_item['bioassembly.id'] = Series(atom.bioassembly.id for atom in self.atom).values
        tmp_item['bioassembly.type'] = Series(atom.bioassembly.type for atom in self.atom).values

        tmp_item.set_index(tmp_item['atom.index'].values)

        self.dataframe = tmp_item

    def extract(self, atom_indices='all'):

        if atom_indices is 'all':
            return self
        else:
            raise NotImplementedError

    def duplicate(self):

        raise NotImplementedError

    def select(self, selection, output_indices='atom'):

        from molmodmt.native.selector import dataframe_select
        indices = dataframe_select(self.dataframe, selection, output_indices=output_indices)
        return indices

