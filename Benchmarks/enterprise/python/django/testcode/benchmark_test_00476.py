# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest00476(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = to_text(header_value)
    return HttpResponse(str(data), content_type='text/html')
