# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest70369(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
