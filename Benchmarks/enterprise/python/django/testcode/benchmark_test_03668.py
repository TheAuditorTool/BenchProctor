# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03668(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    exec(str(data))
    return JsonResponse({"saved": True})
