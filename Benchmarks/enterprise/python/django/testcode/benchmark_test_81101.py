# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest81101(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
