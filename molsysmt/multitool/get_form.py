from molsysmt import puw
from molsysmt.forms import dict_is_form
from molsysmt._private_tools.lists_and_tuples import is_list_or_tuple
from molsysmt._private_tools._digestion import digest_output
from molsysmt.tools.items import item_is_file, item_is_id, item_is_string
from molsysmt.molecular_system import MolecularSystem
from molsysmt._private_tools.exceptions import *

def get_form(molecular_system):

    if type(molecular_system)==MolecularSystem:
        _, output = molecular_system.get_items()
        output = digest_output(output)
        return output

    if puw.is_quantity(molecular_system):

        from molsysmt.forms.classes.api_XYZ import this_Quantity_is_XYZ
        from molsysmt.forms.classes.api_XYZ import form_name as form_XYZ

        if this_Quantity_is_XYZ(molecular_system):
            return form_XYZ
        else:
            raise NotImplementedError()

    if type(molecular_system)==dict:

        from molsysmt.forms.classes.api_dict_molecular_mechanics import this_dict_is_MolecularMechanicsDict
        from molsysmt.forms.classes.api_dict_molecular_mechanics import form_name as form_MolecularMechanicsDict
        from molsysmt.forms.classes.api_dict_simulation import this_dict_is_SimulationDict
        from molsysmt.forms.classes.api_dict_simulation import form_name as form_SimulationDict

        if this_dict_is_MolecularMechanicsDict(molecular_system):
            return form_MolecularMechanicsDict
        elif this_dict_is_SimulationDict(molecular_system):
            return form_SimulationDict
        else:
            raise NotImplementedError()

    if type(molecular_system)==str:

        file_type = item_is_file(molecular_system)
        if file_type:
            return dict_is_form['file:'+file_type]
        id_type = item_is_id(molecular_system)
        if id_type:
            return dict_is_form['id:'+id_type]
        string_type = item_is_string(molecular_system)
        if string_type:
            return dict_is_form['string:'+string_type]

    if is_list_or_tuple(molecular_system):
        output = [get_form(ii) for ii in molecular_system]
        return output

    try:
        return dict_is_form[type(molecular_system)]
    except:
        try:
            return dict_is_form[molecular_system]
        except:
            raise NotImplementedError()

