# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest56931(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
