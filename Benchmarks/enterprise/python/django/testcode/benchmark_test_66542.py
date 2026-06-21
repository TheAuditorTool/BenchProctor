# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66542(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
