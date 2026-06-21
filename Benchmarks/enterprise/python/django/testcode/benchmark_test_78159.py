# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78159(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
