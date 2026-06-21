# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest20003(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = default_blank(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
