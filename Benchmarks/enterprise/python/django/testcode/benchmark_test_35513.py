# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest35513(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
