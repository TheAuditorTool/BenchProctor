# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04172(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
