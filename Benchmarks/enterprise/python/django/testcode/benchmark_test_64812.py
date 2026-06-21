# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest64812(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
