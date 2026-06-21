# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest78294(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(referer_value) + ' -->', content_type='text/html')
