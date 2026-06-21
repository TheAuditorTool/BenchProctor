# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest36213(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return redirect(str(data))
