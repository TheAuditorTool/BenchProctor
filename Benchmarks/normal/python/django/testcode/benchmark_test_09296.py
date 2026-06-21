# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest09296(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    with open('/var/app/data/' + str(header_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
