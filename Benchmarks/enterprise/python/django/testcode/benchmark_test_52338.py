# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


def BenchmarkTest52338(request):
    raw_body = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = raw_body
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
