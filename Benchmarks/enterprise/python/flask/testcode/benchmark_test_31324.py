# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse


def BenchmarkTest31324(path_param):
    path_value = path_param
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(path_value))
    return redirect(target)
