# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest45680(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return redirect(str(data))
