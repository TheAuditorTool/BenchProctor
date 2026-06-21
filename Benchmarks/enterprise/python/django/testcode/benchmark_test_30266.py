# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30266(request):
    raw_body = request.body.decode('utf-8')
    values = str(raw_body).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
