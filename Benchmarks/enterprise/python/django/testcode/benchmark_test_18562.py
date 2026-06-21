# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest18562(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    with open('/var/app/data/' + str(referer_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
