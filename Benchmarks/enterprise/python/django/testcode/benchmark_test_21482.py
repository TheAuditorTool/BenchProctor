# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def BenchmarkTest21482(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
