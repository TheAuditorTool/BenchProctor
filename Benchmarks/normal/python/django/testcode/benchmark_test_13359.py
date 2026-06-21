# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


def BenchmarkTest13359(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = origin_value
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
