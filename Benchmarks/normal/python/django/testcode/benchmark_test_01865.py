# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest01865(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    return HttpResponse(str(data), content_type='text/html')
