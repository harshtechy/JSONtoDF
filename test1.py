import pandas as pd
import json

with open("C:\\Users\\Lenovo\\Downloads\\jsonfile.txt", 'r') as f:
    json_obj = json.load(f).get('data')
flatdict= {}
def flat(obj, v=''):
    #flatdict= {}
    for key, val in obj.items():
        if isinstance(val, dict):
            flat(val,v=v+key)
        elif isinstance(val, list):
            if len(val)==0:
                flatdict[v  + key+ '_'] = val
                continue
            else:
                for i,j in enumerate(val):
                    if isinstance(j, dict):
                        flat(j, v= key+str(i))
                    else:              #k1= v+'_'+i
                        flatdict[v+'_'+str(i)]=j
                        continue
        else:
            flatdict[v  + key+ '_'] = val
            continue
    return flatdict
final = flat(json_obj)
final= pd.DataFrame([final])
print(final)
#
# def flatten_json(json_obj):
#     flattened = {}
#
#     def flatten(inner_obj, name=''):
#         if isinstance(inner_obj, dict):
#             for key, value in inner_obj.items():
#                 flatten(value, name + key + '_')
#         elif isinstance(inner_obj, list):
#              for i, value in enumerate(inner_obj):
#                 flatten(value, name + str(i) + '_')
#         else:
#             flattened[name[:-1]] = inner_obj
#
#     flatten(json_obj)
#     return flattened
#
# # flatten the JSON object
# flattened_json = flatten_json(json_obj)
#
# # convert the flattened JSON to a dataframe
# df = pd.DataFrame([flattened_json])
#
# print(df)
#
