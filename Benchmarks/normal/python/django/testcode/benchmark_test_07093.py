# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest07093(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return redirect(str(data))
