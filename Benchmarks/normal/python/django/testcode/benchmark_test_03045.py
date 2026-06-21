# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest03045(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return HttpResponse(str(data), content_type='text/html')
