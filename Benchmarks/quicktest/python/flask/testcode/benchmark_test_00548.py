# SPDX-License-Identifier: Apache-2.0
from flask import redirect


def BenchmarkTest00548(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return redirect(str(data))
