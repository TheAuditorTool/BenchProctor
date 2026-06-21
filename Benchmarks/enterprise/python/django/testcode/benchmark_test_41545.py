# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41545(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
