# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest04000(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
