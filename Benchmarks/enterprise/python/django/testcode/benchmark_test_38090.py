# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest38090(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    with open('/var/app/data/' + str(forwarded_ip), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
