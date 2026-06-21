# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest10002(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    return HttpResponse(str(data), content_type='text/html')
