# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest54810(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
