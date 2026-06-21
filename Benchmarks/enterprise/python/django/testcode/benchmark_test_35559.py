# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35559(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
