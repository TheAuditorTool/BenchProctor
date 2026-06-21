# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44449(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    int(str(data))
    return JsonResponse({"saved": True})
