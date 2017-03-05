#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace requests_mv_integration

import pytest

from requests_mv_integrations.support.safe_cast import (
    safe_float,
    safe_str,
    safe_dict,
    safe_int,
)


def test_safe_str():
    # test type:
    assert isinstance(safe_str(0), str)
    assert isinstance(safe_str(0.0), str)
    assert isinstance(safe_str('0'), str)
    # test str cast:
    assert safe_str('') == ''
    assert safe_str('Hello Jeff') == 'Hello Jeff'
    assert safe_str('@%#$%^&*') == '@%#$%^&*'
    assert safe_str(None) == ''
    # test numeric cast:
    assert safe_str(0) == '0'
    assert safe_str(10) == '10'
    assert safe_str(-1) == '-1'
    assert safe_str(10.52) == '10.52'
    assert safe_str(-1.32) == '-1.32'


def test_safe_int():
    # test type:
    assert isinstance(safe_int(0), int)
    assert isinstance(safe_int(0.0), int)
    assert isinstance(safe_int('0'), int)
    # test numeric cast:
    assert safe_int(0) == 0
    assert safe_int(10) == 10
    assert safe_int(-1) == -1
    assert safe_int(10.5) == 10
    # test str cast:
    assert safe_int('10') == 10
    assert safe_int('-1') == -1
    assert safe_int('1,000.5') == 1000
    # test default param:
    assert safe_int('###', 256) == 256
    # test exception raising:
    with pytest.raises(ValueError, message='Expecting ValueError to be raised'):
        safe_int('##')


def test_safe_float():
    # test type:
    assert isinstance(safe_float(0), float)
    assert isinstance(safe_float(0.0), float)
    assert isinstance(safe_float('0.0'), float)
    assert isinstance(safe_float('1,252.5'), float)
    # test numeric cast:
    assert safe_float(0) == 0
    assert safe_float(10.52) == 10.52
    assert safe_float(-1) == -1
    assert safe_float(-1.32) == -1.32
    assert safe_float(10.5) == 10.5
    # test str cast:
    assert safe_float('1') == 1
    assert safe_float('-1.32') == -1.32
    assert safe_float('1,152.15') == 1152.15
    # test num values after period:
    assert safe_float(-1.321321, ndigits=6) == -1.321321
    assert safe_float('-1.321321', ndigits=6) == -1.321321
    # test default param:
    assert safe_float('###', default=1.1) == 1.1
    # test exception raising:
    with pytest.raises(ValueError, message='Expecting ValueError to be raised'):
        safe_float('##')


def test_safe_dict():
    # test basic dict:
    assert isinstance(safe_dict({'key': 'value'}), dict)
    # test fail:
    with pytest.raises(TypeError, message='Expecting TypeError because passing not iterable value.'):
        assert safe_dict(5)
    with pytest.raises(ValueError, message='Expecting ValueError because str not castable to dict.'):
        assert safe_dict('Hello Jeff')
