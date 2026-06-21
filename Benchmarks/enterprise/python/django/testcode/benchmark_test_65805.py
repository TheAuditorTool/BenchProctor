# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest65805(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
