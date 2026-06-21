# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest23135(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = origin_value
    return HttpResponse(str(processed), content_type='text/html')
