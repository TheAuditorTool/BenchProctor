# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36035(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
