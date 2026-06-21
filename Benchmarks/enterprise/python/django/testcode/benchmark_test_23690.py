# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest23690(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
