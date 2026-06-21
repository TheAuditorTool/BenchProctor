# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def normalise_input(value):
    return value.strip()

def BenchmarkTest74544(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
