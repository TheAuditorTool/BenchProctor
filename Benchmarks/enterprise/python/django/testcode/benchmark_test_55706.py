# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest55706(request):
    host_value = request.META.get('HTTP_HOST', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(host_value) + ' -->', content_type='text/html')
