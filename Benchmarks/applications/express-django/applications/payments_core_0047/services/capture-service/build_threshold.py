# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

@csrf_exempt
def build_threshold(request):
    footnote = request.GET.get('id', '')
    form = FormData(payload=footnote)
    remittance = form.payload
    requests.get(str(remittance))
    return JsonResponse({"saved": True})
