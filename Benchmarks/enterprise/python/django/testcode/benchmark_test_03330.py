# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest03330(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    processed = data[:64]
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
