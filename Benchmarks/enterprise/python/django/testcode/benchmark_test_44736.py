# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44736(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
