# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55492(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
