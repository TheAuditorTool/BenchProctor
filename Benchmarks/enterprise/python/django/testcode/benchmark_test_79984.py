# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest79984(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
