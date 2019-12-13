
def from_molmodmt_DataFrame(item, atom_indices='all', frame_indices='all'):

    from molmodmt.native import Composition
    from molmodmt.native import elements
    from molmodmt import extract

    dataframe = extract(item, atom_indices=atom_indices, frame_indices=frame_indices)

    tmp_item = Composition()

    atom_counter = 0
    atom_index = 0
    atom_old_indices_added = set()
    atom_old_index_to_new_index = {}

    group_counter = 0
    group_index = 0
    group_old_indices_added = set()
    group_old_index_to_new_index = {}

    component_counter = 0
    component_index = 0
    component_old_indices_added = set()
    component_old_index_to_new_index = {}

    chain_counter = 0
    chain_index = 0
    chain_old_indices_added = set()
    chain_old_index_to_new_index = {}

    for row_index, row in dataframe.iterrows():

        atom_old_index = row['atom.index']
        group_old_index = row['group.index']
        component_old_index = row['component.index']
        chain_old_index = row['chain.index']
        molecule_old_index = row['molecule.index']
        entity_old_index = row['entity.index']
        bioassembly_old_index = row['bioassembly.index']

        # Adding atom

        atom_index = atom_counter
        atom = elements.Atom(index=atom_index, id=row['atom.id'], name=row['atom.name'], type=row['atom.type'])
        atom_old_indices_added.add(atom_old_index)
        atom_old_index_to_new_index[atom_old_index] = atom_index
        tmp_item.atom.append(atom)
        atom_counter += 1

        # Adding group if needed

        if group_old_index not in group_old_indices_added:

            group_index = group_counter
            group = elements.group_initialization_wizard((index=group_index, id=row['group.id'], name=row['group.name'], type=row['group.type'])
            group_old_indices_added.add(group_old_index)
            group_old_index_to_new_index[old_group_index]=group_index
            tmp_item.group.append(group)
            group_counter += 1

        else:

            group_index = group_old_index_to_new_index[group_old_index]
            group = tmp_item.group[group_index]

        # Adding component if needed

        if component_old_index not in component_old_indices_added:

            component_index = component_counter
            component = elements.Component(index=component_index, id=row['component.id'], name=row['component.name'], type=row['component.type'])
            component_old_indices_added.add(component_old_index)
            component_old_index_to_new_index[component_old_index]=component_index
            tmp_item.component.append(component)
            component_counter += 1

        else:

            component_index = component_old_index_to_new_index[component_old_index]
            component = tmp_item.component[component_index]

        # Adding chain if needed

        if chain_old_index not in chain_old_indices_added:

            chain_index = chain_counter
            chain = elements.Chain(index=chain_index, id=row['chain.id'], name=row['chain.name'], type=row['chain.type'])
            chain_old_indices_added.add(chain_old_index)
            chain_old_index_to_new_index[chain_old_index]=chain_index
            tmp_item.chain.append(chain)
            chain_counter += 1

        else:

            chain_index = chain_old_index_to_new_index[chain_old_index]
            chain = tmp_item.chain[chain_index]

        # Adding molecule if needed

        if molecule_old_index not in molecule_old_indices_added:

            molecule_index = molecule_counter
            molecule = elements.molecule_initialization_wizard(index=molecule_index, id=row['molecule.id'], name=row['molecule.name'], type=row['molecule.type'])
            molecule_old_indices_added.add(molecule_old_index)
            molecule_old_index_to_new_index[molecule_old_index]=molecule_index
            tmp_item.molecule.append(molecule)
            molecule_counter += 1

        else:

            molecule_index = molecule_old_index_to_new_index[molecule_old_index]
            molecule = tmp_item.molecule[molecule_index]

        # Adding entity if needed

        if entity_old_index not in molecule_old_indices_added:

            entity_index = entity_counter
            entity = elements.entity_initialization_wizard(index=entity_index, id=row['entity.id'], name=row['entity.name'], type=row['entity.type'])
            entity_old_indices_added.add(entity_old_index)
            entity_old_index_to_new_index[entity_old_index]=entity_index
            tmp_item.entity.append(entity)
            entity_counter += 1

        else:

            entity_index = entity_old_index_to_new_index[entity_old_index]
            entity = tmp_item.entity[entity_index]

        # Adding bioassembly if needed

        if bioassembly_old_index not in bioassembly_old_indices_added:

            bioassembly_index = bioassembly_counter
            bioassembly = elements.Bioassembly(index=bioassembly_index, id=row['bioassembly.id'], name=row['bioassembly.name'], type=row['bioassembly.type'])
            bioassembly_old_indices_added.add(bioassembly_old_index)
            bioassembly_old_index_to_new_index[bioassembly_old_index]=bioassembly_index
            tmp_item.bioassembly.append(bioassembly)
            bioassembly_counter += 1

        else:

            bioassembly_index = entity_old_index_to_new_index[bioassembly_old_index]
            bioassembly = tmp_item.bioassembly[bioassembly_index]

        # Complete Composition Structure

        atom.group = group
        group.append(atom)
        atom.component = component
        component.append(atom)
        atom.chain = chain
        chain.append(atom)
        atom.molecule = molecule
        molecule.append(atom)
        atom.entity = entity
        entity.append(atom)
        atom.bioassembly = bioassembly
        bioassembly.append(atom)



