# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest54918(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(header_value) + ' -->', content_type='text/html')
