# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05541(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
