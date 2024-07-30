__doc__ = "This is a Code snippet for adding shared parameters to the Family Instances of the active Revit Document"
__author__ = 'Abhishek Shinde | Silman Colab'
__contact__ = 'abhishek.shinde@silman.com | arabhishek1091@gmail.com'
__copyright__ = 'SILMAN COLAB- Silman Structural Solutions'
__license__ = "M.I.T. License"

"""
Please credit the author when using the code snippets 
""" 

from Autodesk.Revit.DB import Transaction, StorageType, SharedParameterElement, FamilyInstance, CategorySet, InstanceBinding, TypeBinding, BuiltInCategory, ElementMulticategoryFilter, FilteredElementCollector
from System.Collections.Generic import List

# Specify the user categories 
requiredcategories = List[BuiltInCategory]([
    BuiltInCategory.OST_StructuralColumns,
    BuiltInCategory.OST_StructuralFoundation,
    BuiltInCategory.OST_StructuralFraming,
    BuiltInCategory.OST_Walls,
    BuiltInCategory.OST_Floors,
    BuiltInCategory.OST_Roofs
])

# Create a custom filter to feed to our element collection
custom_filter = ElementMulticategoryFilter(requiredcategories)

# Create a Filtered Element Collector to get all family instances
activerevitDoc_ectcustomcategory_elements_tomodify = FilteredElementCollector(doc).OfClass(FamilyInstance).WherePasses(custom_filter)

def addSharedParamsToFamilyInstances(doc, family_instances, famDefs, famBipgs, famInst, famForm):
    all_params = {}

    t = Transaction(doc, "Add Shared Parameters to Categories")
    t.Start()

    try:
        # Bind all parameters to the specified categories
        category_set = CategorySet()
        for cat in requiredcategories:
            category_set.Insert(doc.Settings.Categories.get_Item(cat))

        for d, b, i in zip(famDefs, famBipgs, famInst):
            try:
                shared_param_element = SharedParameterElement.Lookup(doc, d.GUID)
                if shared_param_element is None:
                    print("Shared parameter {} not found in the project.".format(d.Name))
                    continue

                binding = InstanceBinding(category_set) if i else TypeBinding(category_set)
                binding_map = doc.ParameterBindings
                if binding_map.Contains(d):
                    binding_map.Remove(d)
                binding_map.Insert(d, binding, b)
            except Exception as e:
                print("Error binding parameter {}: {}".format(d.Name, str(e)))

        # Now, set values for the parameters
        for instance in family_instances:
            if not isinstance(instance, FamilyInstance):
                print("Skipping non-family instance: {}".format(instance.Id))
                continue

            family_name = instance.Symbol.Family.Name
            params = []

            for d, f in zip(famDefs, famForm):
                try:
                    param = instance.LookupParameter(d.Name)
                    if param:
                        if f is not None:
                            if param.IsReadOnly:
                                print("Parameter {} is read-only for instance {}".format(d.Name, instance.Id))
                            else:
                                if param.StorageType == StorageType.String:
                                    param.Set(f)
                                elif param.StorageType == StorageType.Double:
                                    param.Set(float(f))
                                elif param.StorageType == StorageType.Integer:
                                    param.Set(int(f))
                            params.append(d.Name)
                    else:
                        print("Parameter {} not found for instance {}".format(d.Name, instance.Id))
                except Exception as e:
                    print("Error setting value for parameter {}: {}".format(d.Name, str(e)))

            if params:
                all_params[family_name] = params

    except Exception as e:
        print("Error during transaction: {}".format(str(e)))
        t.RollBack()
    else:
        t.Commit()

    return all_params

# Call the function
result = addSharedParamsToFamilyInstances(doc, activerevitDoc_ectcustomcategory_elements_tomodify, fam_defs, fam_bipgs, fam_instances, fam_formulae)
