# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31838(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
