# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest63920(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
