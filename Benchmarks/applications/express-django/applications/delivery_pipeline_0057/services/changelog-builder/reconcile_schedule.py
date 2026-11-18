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
def reconcile_schedule(request):
    footnote = request.META.get('HTTP_ORIGIN', '')
    wording = RequestPayload(footnote).value
    parsed = json.loads(wording)
    return JsonResponse({'parsed': str(parsed)}, status=200)
