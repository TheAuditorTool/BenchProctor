# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest52588(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
