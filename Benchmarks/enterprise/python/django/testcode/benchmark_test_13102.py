# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import time


def relay_value(value):
    return value

def BenchmarkTest13102(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
