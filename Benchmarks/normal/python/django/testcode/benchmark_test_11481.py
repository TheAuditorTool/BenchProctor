# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def ensure_str(value):
    return str(value)

def BenchmarkTest11481(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
