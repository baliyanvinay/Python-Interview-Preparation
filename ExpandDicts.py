# From a given nested dict, normalize it into dict.

def normalize_dict(input_dict):
    '''
    Expanding nested dicts into normalized dict using recursion
    '''
    result = {}
    for key, val in input_dict.items():
        if isinstance(val, dict):
            result.update(normalize_dict(val))
        else:
            result[key] = val

    return result


sample_dict = {
        "key1": "val1", 
        "key2": {
            "key2_1": "val2_1", 
            "key2_2": {
                "key2_2_1": "val2_2_1",
                "key2_2_2": "val2_2_2",
                },
            "key2_3": "val2_3"
            },
        "key3": "val3",
        "key4": "val4"
        }

output_dict = normalize_dict(sample_dict)
print(output_dict)

## Expected Output
# output_dict = {
#     "key1": "val1",
#     "key2_1": "val2_1",
#     "key2_2_1": "val2_2_1",
#     "key2_2_2": "val2_2_2",
#     "key2_3": "val2_3",
#     "key3": "val3",
#     "key4": "val4"
# }