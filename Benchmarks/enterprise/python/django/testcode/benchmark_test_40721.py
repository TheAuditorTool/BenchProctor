# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest40721(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    return HttpResponse(str(data), content_type='text/html')
