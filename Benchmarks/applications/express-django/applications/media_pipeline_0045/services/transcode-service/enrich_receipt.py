# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

@csrf_exempt
def enrich_receipt(request):
    notice = request.META.get('HTTP_ORIGIN', '')
    rendition = RequestPayload(notice).value
    parsed = json.loads(rendition)
    return JsonResponse({'parsed': str(parsed)}, status=200)
