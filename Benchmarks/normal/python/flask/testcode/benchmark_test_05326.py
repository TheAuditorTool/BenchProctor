# SPDX-License-Identifier: Apache-2.0


def relay_value(value):
    return value

def BenchmarkTest05326(path_param):
    path_value = path_param
    data = relay_value(path_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
