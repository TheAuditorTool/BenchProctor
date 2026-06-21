# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest34161(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(ua_value) + ' -->', content_type='text/html')
