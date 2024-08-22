import typing

def compress_json_to_tuples(
    result: typing.List[typing.Dict],
    condensed: bool = True,
    fields: typing.Optional[typing.Tuple[str, ...]] = None
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Compress JSON data into machine-readable tuples of tuples.

    :param result: List of dictionaries containing JSON data
    :param condensed: If True, return tuple of tuples; else, list of dicts (default: True)
    :param fields: Optional tuple of field names to include in the output
    :return: Compressed data as tuple of tuples or original list of dicts
    """
    if result is not None and condensed:
        if result:
            if fields is None:
                # Get all unique keys from the result if fields are not specified
                fields = tuple(set(key for entry in result for key in entry.keys()))
            
            # Convert each entry to a tuple, preserving order of fields
            compact_result = tuple(
                tuple(str(entry.get(field, '')) for field in fields)
                for entry in result
            )
            
            return (fields,) + compact_result
        else:
            return ((),)  # Return an empty tuple of tuples if result is empty
    else:
        return result