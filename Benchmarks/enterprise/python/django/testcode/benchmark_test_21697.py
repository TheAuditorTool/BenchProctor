# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest21697(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
