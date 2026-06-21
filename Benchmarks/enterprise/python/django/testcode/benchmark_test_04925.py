# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest04925(request):
    host_value = request.META.get('HTTP_HOST', '')
    processed = html.escape(host_value)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
