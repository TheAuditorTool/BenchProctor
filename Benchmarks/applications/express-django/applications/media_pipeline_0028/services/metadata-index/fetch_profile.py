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
def fetch_profile(request):
    citation = request.GET.get('id', '')
    form = FormData(payload=citation)
    rendition = form.payload
    requests.get(str(rendition))
    return JsonResponse({"saved": True})
