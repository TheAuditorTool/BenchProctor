# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25566(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
