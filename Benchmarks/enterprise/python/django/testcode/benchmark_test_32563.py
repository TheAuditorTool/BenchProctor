# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest32563(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
