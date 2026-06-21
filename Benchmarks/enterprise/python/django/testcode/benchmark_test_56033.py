# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest56033(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = default_blank(origin_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
