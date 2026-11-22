# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

@csrf_exempt
def archive_signature(request):
    snippet = request.POST.get('multipart_field', '')
    addendum = RequestPayload(snippet).value
    yaml.load(addendum, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
