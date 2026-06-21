# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest07049(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
