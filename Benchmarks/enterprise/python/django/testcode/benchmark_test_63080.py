# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest63080(request, path_param):
    path_value = path_param
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(path_value))
    return redirect(target)
