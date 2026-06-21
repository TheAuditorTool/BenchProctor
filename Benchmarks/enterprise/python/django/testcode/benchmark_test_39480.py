# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39480(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
