__doc__ = "This is a Code snippet for adding shared parameters to the Family Instances of the active Revit Document"
__author__ = 'Abhishek Shinde | Silman Colab'
__contact__ = 'abhishek.shinde@silman.com | arabhishek1091@gmail.com'
__copyright__ = 'SILMAN COLAB- Silman Structural Solutions'
__license__ = "M.I.T. License"
__version__ = "1.0"
__credits__ = "Aussie BIM Guru"

"""
ABOUT

Please credit the author when using the code snippets.
This version only applies shared parameter with 
Try using the v2 for your project, as it applies the shared parameters to both 
the family instances and the System Families in the active Revit Document

This function is modified from the "AddSharedParameters" Youtube tutorial by AussieBIMGuru 

""" 

from Autodesk.Revit.DB import Transaction, StorageType, SharedParameterElement, FamilyInstance, CategorySet, InstanceBinding, TypeBinding, BuiltInCategory

def addSharedParamsToFamilyInstances(family_instances, famDefs, famBipgs, famInst, famForm):
    all_params = {}

    t = Transaction(doc, "Add Shared Parameters to Family Instances")
    t.Start()

    try:
        for instance in family_instances:
            if not isinstance(instance, FamilyInstance):
                print("Skipping non-family instance: {}".format(instance.Id))
                continue

            family_name = instance.Symbol.Family.Name
            params = []
            existing_params = [p.Definition.Name for p in instance.Parameters]

            category = instance.Category
            category_set = CategorySet()
            category_set.Insert(category)

            for d, b, i, f in zip(famDefs, famBipgs, famInst, famForm):
                if d.Name not in existing_params:
                    try:
                        shared_param_element = SharedParameterElement.Lookup(doc, d.GUID)
                        if shared_param_element is None:
                            print("Shared parameter {} not found in the project.".format(d.Name))
                            continue

                        # Create binding
                        binding = InstanceBinding(category_set) if i else TypeBinding(category_set)

                        # Add the binding
                        doc.ParameterBindings.Insert(d, binding, b)

                        # Set the value for the parameter
                        param = instance.LookupParameter(d.Name)
                        if param:
                            if f is not None:
                                if param.StorageType == StorageType.String:
                                    param.Set(f)
                                elif param.StorageType == StorageType.Double:
                                    param.Set(float(f))
                                elif param.StorageType == StorageType.Integer:
                                    param.Set(int(f))
                            params.append(d.Name)
                        else:
                            print("Parameter {0} not found after adding.".format(d.Name))

                    except Exception as e:
                        print("Error adding parameter {0}: {1}".format(d.Name, str(e)))

            if params:
                all_params[family_name] = params

    except Exception as e:
        print("Error during transaction: {0}".format(str(e)))
        t.RollBack()
    else:
        t.Commit()

    return all_params

#Apply the Function for adding shared parameters and formulae to the active family Document
addSharedParamsToFamilyInstances(activerevitDoc_ectcustomcategory_elements_tomodify, fam_defs, fam_bipgs, fam_instances, fam_formulae)