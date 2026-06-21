# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest14557(request):
    xml_value = request.body.decode('utf-8')
    globals()['counter'] = int(xml_value)
    return JsonResponse({"saved": True})
