def replace_values(old, new):
    for key, value in new.items():
        if type(value) is str:
            new[key] = _get_value_from_dictionary_by_def(old, value)
        else:
            new[key] = replace_values(old, new[key])

    return new


def _get_value_from_dictionary_by_def(dictionary, definition):
    keys = definition.split('.')
    value = dictionary

    for key in keys:
        value = value[key]

    return value
