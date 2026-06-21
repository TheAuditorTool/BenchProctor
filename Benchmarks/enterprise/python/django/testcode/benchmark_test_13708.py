# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest13708(request):
    xml_value = request.body.decode('utf-8')
    os.remove(str(xml_value))
    return JsonResponse({"saved": True})
