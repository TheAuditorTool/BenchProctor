# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62581(request, path_param):
    path_value = path_param
    processed = 'true' if str(path_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
