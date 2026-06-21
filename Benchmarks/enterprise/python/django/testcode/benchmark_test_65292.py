# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest65292(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = normalise_input(ua_value)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
