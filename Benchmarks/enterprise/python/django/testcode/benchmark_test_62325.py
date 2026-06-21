# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest62325(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    with open('/var/app/data/' + str(ua_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
