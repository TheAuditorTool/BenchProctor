# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest32912(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    return HttpResponse(str(processed), content_type='text/html')
