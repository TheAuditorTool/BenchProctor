# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest70752(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
