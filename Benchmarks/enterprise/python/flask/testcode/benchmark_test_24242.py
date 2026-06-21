# SPDX-License-Identifier: Apache-2.0
from flask import redirect


def BenchmarkTest24242(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return redirect(str(data))
