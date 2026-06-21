# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse


def BenchmarkTest40551(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
