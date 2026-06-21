# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest47665(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
