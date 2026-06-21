# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56843(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
