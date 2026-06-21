# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def normalise_input(value):
    return value.strip()

def BenchmarkTest38232(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
