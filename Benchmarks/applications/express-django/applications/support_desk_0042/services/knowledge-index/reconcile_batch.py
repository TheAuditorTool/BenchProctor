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
def reconcile_batch(request):
    blurb = request.GET.get('id', '')
    form = FormData(payload=blurb)
    inquiry = form.payload
    requests.get(str(inquiry))
    return JsonResponse({"saved": True})
