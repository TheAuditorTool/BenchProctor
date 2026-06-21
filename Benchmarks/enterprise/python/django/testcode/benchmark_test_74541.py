# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


def BenchmarkTest74541(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(header_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = header_value
    return HttpResponse(Template(processed).render(Context()))
