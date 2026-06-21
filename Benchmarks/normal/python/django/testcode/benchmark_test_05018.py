# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest05018(request):
    user_id = request.GET.get('id', '')
    data = RequestPayload(user_id).value
    return redirect(str(data))
