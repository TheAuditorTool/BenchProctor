# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest02151(request):
    raw_body = request.body.decode('utf-8')
    if raw_body not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = raw_body
    return HttpResponse(str(processed), content_type='text/html')
