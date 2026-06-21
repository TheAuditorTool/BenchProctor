# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest39180(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
