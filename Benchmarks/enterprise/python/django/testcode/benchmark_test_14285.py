# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14285(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
