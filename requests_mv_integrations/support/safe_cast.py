#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace request_mv_integration


def safe_cast(val, to_type, default=None):
    """Safely cast value to type, and if failed, returned default if exists.
        If default is 'None' and and error occurs, it is raised.

    Args:
        val:
        to_type:
        default:

    Returns:

    """
    if val is None:
        return default

    try:
        return to_type(val)
    except ValueError as ex:
        if default is not None:
            return default
        else:
            raise ex


def safe_str(val, default=None):
    """Safely cast value to str, Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    if val is None:
        return ''
    return safe_cast(val, str, default)


def safe_float(val, ndigits=2, default=None):
    """Safely cast value to float, remove ',' if exists to ensure strs like: "1,234.5" are handled
        Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        ndigits:
        default:

    Returns:

    """
    tmp_val = val.replace(',', '') if type(val) == str else val
    return round(safe_cast(tmp_val, float, default), ndigits)


def safe_int(val, default=None):
    """Safely cast value to int. Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    return safe_cast(safe_float(val, ndigits=0, default=default), int, default)


def safe_dict(val, default=None):
    """Safely cast value to dict. Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    return safe_cast(val, dict, default)

