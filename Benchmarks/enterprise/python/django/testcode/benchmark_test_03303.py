# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def ensure_str(value):
    return str(value)

def BenchmarkTest03303(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
