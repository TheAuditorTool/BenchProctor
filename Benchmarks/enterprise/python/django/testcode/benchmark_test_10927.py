# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest10927(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    return HttpResponse(str(data), content_type='text/html')
