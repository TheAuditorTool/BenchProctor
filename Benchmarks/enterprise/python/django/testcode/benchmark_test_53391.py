# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest53391(request):
    host_value = request.META.get('HTTP_HOST', '')
    with open('/var/app/data/' + str(host_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
