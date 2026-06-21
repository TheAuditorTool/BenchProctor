# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15140(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
