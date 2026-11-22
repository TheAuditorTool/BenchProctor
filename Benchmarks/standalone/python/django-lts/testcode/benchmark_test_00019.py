# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00019(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return redirect(str(data))
