# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest58560(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    processed = html.escape(referer_value)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
