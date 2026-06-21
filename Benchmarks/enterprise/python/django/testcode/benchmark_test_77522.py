# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77522(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
