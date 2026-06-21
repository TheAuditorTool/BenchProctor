# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02924(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
