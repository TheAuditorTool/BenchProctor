# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest73571(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
