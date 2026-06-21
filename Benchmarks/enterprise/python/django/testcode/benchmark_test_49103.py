# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest49103(request):
    xml_value = request.body.decode('utf-8')
    with open('/var/app/data/' + str(xml_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
