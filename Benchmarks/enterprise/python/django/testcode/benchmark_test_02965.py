# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02965(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
