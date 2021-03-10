import numpy as np
from molsysmt import puw

def charge(molecular_system, target='group', selection = 'all', type='physical_pH7', forcefield=None, engine='OpenMM'):

    from molsysmt._private_tools._digestion import digest_engine, digest_target

    engine=digest_engine(engine)
    target=digest_target(target)

    if forcefield is None and type in ['physical_pH7', 'collantes']:

        from molsysmt.multitool import get

        from .residues.charge import units
        if type=='physical_pH7':
            from .residues.charge import physical_pH7 as values, units
        elif type=='collantes':
            from .residues.charge import collantes as values, units

        output = []

        if target=='atom':
            raise ValueError('Only targets bigger than, or equal to, groups are allowed when type is "physical_pH7" or "collantes"')

        elif target=='group':

            group_names = get(molecular_system, target = target, selection = selection, group_name = True)
            for ii in group_names:
                output.append(values[ii.upper()])

        elif target in ['component', 'molecule', 'chain', 'entity']:

            group_names = get(molecular_system, target = target, selection = selection, group_name = True)
            for aux in group_names:
                output.append(np.sum([values[ii.upper()] for ii in aux]))

        elif target=='system':

            group_names = get(molecular_system, target = 'group', selection = 'all', group_names = True)
            output.append(np.sum([values[ii.upper()] for ii in group_names]))

        if target =='system':
            output = output[0]*puw.unit(units)
        else:
            output = puw.quantity(np.array(output), units)

    elif type=='ForceField':

        from molsysmt.multitool import get, convert, get_form

        if engine == 'OpenMM':

            if forcefield is not None:

                openmm_system = convert(molecular_system, to_form='openmm.System', forcefield=forcefield)

            else:

                from molsysmt import get_form
                if get_form(molecular_system)!='openmm.System':
                    raise ValueError('The molecular_system is not an openmm.System object. A value for the \
                                      input argument forcefield is needed if engine=="OpenMM"')
                else:
                    openmm_system = molecular_system

            if target=='atom':

                atom_indices = get(molecular_system, target = target, selection = selection, atom_index = True)

                for force_index in range(system.getNumForces()):
                    force = system.getForce(force_index)
                    if isinstance(force, NonbondedForce):
                        for index in atom_indices:
                            output.append(force.getParticleParameters(int(index))[0]._value)

                output = np.array(output, dtype=float)*puw.unit('e')

            elif target in ['group', 'component', 'chain', 'molecule', 'entity']:

                atom_indices = get(molecular_system, target = target, selection = selection, atom_index = True)

                for force_index in range(system.getNumForces()):
                    force = system.getForce(force_index)
                    if isinstance(force, NonbondedForce):
                        for atom_list in atom_indices:
                            var_aux = 0.0
                            for index in atom_list:
                                var_aux+=force.getParticleParameters(int(index))[0]._value
                            output.append(var_aux)

                output = np.array(output, dtype=float)*puw.unit('e')

            elif target=='system':

                atom_indices = get(molecular_system, target = 'atom', selection = 'all', index = True)

                var_aux = 0.0
                for force_index in range(system.getNumForces()):
                    force = system.getForce(force_index)
                    if isinstance(force, NonbondedForce):
                        for index in atom_indices:
                            var_aux+=force.getParticleParameters(int(index))[0]._value

                #output = int(round(var_aux))*unit.elementary_charge
                output = var_aux*puw.charge('e')

    else:
        raise NotImplementedError

    return output
