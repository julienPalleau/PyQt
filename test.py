list_essai = [{'experiment_procedure1': {'id': 1508, 'name': 'Description', 'section_type': 'description',
                                         'collapsed': False, 'time_range': None, 'elements':
                                             [{'id': 2442, 'uuid': '9cd64bc8-59de-4deb-9aa9-493f366a938e',
                                               'element_type': 'text', 'rows': None, 'cols': None, 'name': None}],
                                         'start_date': None, 'end_date': None,
                                         'uuid': 'c2d0de73-8981-4bf6-9ded-07821d709654'}}, {
                  'experiment_procedure2': {'id': 1509, 'name': 'Procedure', 'section_type': 'procedure',
                                            'collapsed': False, 'time_range': None, 'elements':
                                                [{'id': 2443, 'uuid': '62aae41e-bd9f-4dd5-954b-14bf59183319',
                                                  'element_type': 'form', 'rows': None, 'cols': None, 'name': 'Form'}],
                                            'start_date': None, 'end_date': None,
                                            'uuid': '32f1b8d6-b21d-463f-888f-3ee2ee694fb2'}}, {
                  'experiment_procedure3': {'id': 1510, 'name': 'Medium', 'section_type': 'custom', 'collapsed': False,
                                            'time_range': None, 'elements':
                                                [{'id': 2444, 'uuid': '5666e14e-15bf-49e9-895d-6c214e9eca19',
                                                  'element_type': 'samples', 'rows': None, 'cols': None,
                                                  'name': 'Samples & Reagents'}],
                                            'start_date': None, 'end_date': None,
                                            'uuid': '9e718e56-c420-43eb-9546-2efe6128611a'}}, {
                  'experiment_procedure4': {'id': 1511, 'name': 'Results', 'section_type': 'results',
                                            'collapsed': False,
                                            'time_range': None, 'elements':
                                                [{'id': 2445, 'uuid': '1eadcd2f-7d17-422c-8103-dc2f18922753',
                                                  'element_type': 'text', 'rows': None, 'cols': None, 'name': None}],
                                            'start_date': None, 'end_date': None,
                                            'uuid': 'd101a38b-2940-4d82-93f2-15cd7e175c30'}}]

# print(f"longuer de la liste: {len(list_essai)}")
# print(f"list_essai: {list_essai}\n")

# def trawler(list_essai):
#     print(f'Debug 0 : {list_essai}')
#     if isinstance(list_essai, str):
#         print(f'Debug 1 : {list_essai}')
#
#     elif isinstance(list_essai, list):
#         print("Debug 2 : list niveau 1")
#         if len(list_essai) > 0:
#             x = list_essai.pop(0)
#             print(f"{x}\n")
#             if isinstance(x, list):
#                 print("Debug 3 : list niveau 3")
#             elif isinstance(x, dict):
#                 for key, value in x.items():
#                     print(f'Debug 4 : key1---> {key}, value1---> {value}')
#                     trawler(value)
#             else:
#                 print("Debug 5 : Error_1")
#         elif isinstance(list_essai, dict):
#             print("Debug 6 : list niveau 2")
#             for key, value in list_essai.items():
#                 print(f'Debug 7 : key2---> {key}, value2---> {value}')
#                 trawler(list_essai)
#     elif isinstance(list_essai, dict):
#         print(f"Debug 8 : list_essai last {list_essai}")
#         for key, value in list_essai.items():
#             print(f'Debug 9 : key3---> {key}, value3---> {value}')
#             trawler(value)
#     elif isinstance(list_essai, str):
#         print(f'Debug 10 : ERROR_2')
#
#
# trawler(list_essai)

list2_essai = {'experiment_procedure1': {'member_id':0, 'id': 1508, 'name': 'Description', 'section_type': 'description',
                                         'collapsed': False, 'time_range': None,
                                         'start_date': None, 'end_date': None,
                                         'uuid': 'c2d0de73-8981-4bf6-9ded-07821d709654'},

               'experiment_procedure2': {'id': 1509, 'name': 'Procedure', 'section_type': 'procedure',
                                         'collapsed': False, 'time_range': None,
                                         'start_date': None, 'end_date': None,
                                         'uuid': '32f1b8d6-b21d-463f-888f-3ee2ee694fb2'},

               'experiment_procedure3': {'id': 1510, 'name': 'Medium', 'section_type': 'custom', 'collapsed': False,
                                         'time_range': None,
                                         'start_date': None, 'end_date': None,
                                         'uuid': '9e718e56-c420-43eb-9546-2efe6128611a'},

               'experiment_procedure4': {'id': 1511, 'name': 'Results', 'section_type': 'results',
                                         'collapsed': False,
                                         'time_range': None}
               }

students = {
    'ID 1': {'Name': 'Shaun', 'Age': 35, 'City': 'Delhi'},
    'ID 2': {'Name': 'Ritika', 'Age': 31, 'City': 'Mumbai'},
    'ID 3': {'Name': 'Smriti', 'Age': 33, 'City': 'Sydney'},
    'ID 4': {'Name': 'Jacob', 'Age': 23, 'City': {'perm': 'Tokyo',
                                                  'current': 'London'}},
}

result = []


# def nested_dict_pairs_iterator(dict_obj):
#     ''' This function accepts a nested dictionary as argument
#         and iterate over all values of nested dictionaries
#     '''
#     # Iterate over all key-value pairs of dict argument
#     if isinstance(dict_obj, dict):
#         for key, value in dict_obj.items():
#             # Check if value is of dict type
#             if isinstance(value, dict):
#                 # If value is dict then iterate over all its values
#                 for pair in nested_dict_pairs_iterator(value):
#                     yield (key, *pair)
#             else:
#                 # If value is not dict type then yield the value
#                 yield (key, value)
#     elif isinstance(dict_obj, list):
#         print("this is a list")
#         for line in dict_obj:
#             if isinstance(line, dict):
#                 print("test1")
#                 for key, value in line.items():
#                     # Check if value is of dict type
#                     print(f"key --> {key}, value --> {value}")
#                     if isinstance(value, dict):
#                         # If value is dict then iterate over all its values
#                         for pair in nested_dict_pairs_iterator(value):
#                             yield (key, *pair)
#                     else:
#                         # If value is not dict type then yield the value
#                         yield (key, value)
#
#
#
#
#
# # Loop through all key-value pairs of a nested dictionary
# for pair in nested_dict_pairs_iterator(list_essai):
#     print(pair)

def get_id(value, keyword: str):
    id_list = []
    if isinstance(value, dict):
        # get id if exist from dict
        if id := value.get(keyword):
            id_list += [id]

        # get id's from nested list or dicts
        for val in value.values():
            if isinstance(val, list) or isinstance(val, dict):
                id_list += get_id(val, keyword)

    if isinstance(value, list):
        for val in value:
            if isinstance(val, list) or isinstance(val, dict):
                id_list += get_id(val, keyword)

    return id_list


print(get_id(list_essai, "id"))
print("done")
