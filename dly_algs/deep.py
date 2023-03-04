from copy import deepcopy


def deep_merge(x_dict: dict, y_dict: dict) -> dict:
    """
    Deep merges two dictionaries. The y_dict will overwrite the values of the x_dict, if both have conflicting values.
    The function will also respect nested structures like below:

    x_dict = {"a": 1, "b": {"c": 1, "d": 1}}

    y_dict = {"b": {"c": 2, "e": 2}}

    z_dict = deep_merge(x_dict, y_dict)

    z_dict # {"a": 1, "b": {"c": 2, "d": 1, "e": 2}}

    :param x_dict: Specifies the first dictionary to be deep merged.
    :param y_dict: Specifies the second dictionary to be deep merged.
    :return: A merged deep copy of both passed dictionaries.
    """
    old_dict = deepcopy(x_dict)
    new_dict = deepcopy(y_dict)
    for new_key, new_value in new_dict.items():
        if isinstance(new_value, dict) and new_key in old_dict:
            old_dict[new_key] = deep_merge(old_dict[new_key], new_value)
        else:
            old_dict[new_key] = new_value
    return old_dict


def deep_compare(x_dict: dict, y_dict: dict) -> bool:
    """
    Deep compares the content of two dictionaries.

    :param x_dict: Specifies the first dictionary to be deep compared.
    :param y_dict: Specifies the second dictionary to be deep compared.
    :return: A bool specifying if the dictionaries are equal.
    """
    if isinstance(x_dict, dict) and isinstance(y_dict, dict):
        return all(deep_compare(x_dict.get(key), y_dict.get(key)) for key in set(x_dict).union(y_dict))
    return x_dict == y_dict
