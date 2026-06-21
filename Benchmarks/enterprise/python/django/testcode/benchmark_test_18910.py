# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18910(request):
    xml_value = request.body.decode('utf-8')
    request.session['data'] = str(xml_value)
    return JsonResponse({"saved": True})
