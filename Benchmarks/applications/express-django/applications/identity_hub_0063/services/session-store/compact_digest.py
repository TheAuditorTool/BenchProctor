# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

@csrf_exempt
def compact_digest(request):
    paragraph = request.COOKIES.get('session_token', '')
    persona = RequestPayload(paragraph).value
    requests.get(str(persona))
    return JsonResponse({"saved": True})
