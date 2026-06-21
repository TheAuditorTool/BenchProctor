# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36209(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
