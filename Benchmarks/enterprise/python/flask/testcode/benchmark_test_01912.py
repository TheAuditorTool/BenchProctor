# SPDX-License-Identifier: Apache-2.0
from flask import redirect


def BenchmarkTest01912(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return redirect(str(data))
