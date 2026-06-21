# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse


def BenchmarkTest45286(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
