# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

@csrf_exempt
def normalize_bundle(request):
    heading = os.environ.get('PUBLISHING_INPUT_0003', '')
    addendum = RequestPayload(heading).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, addendum))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    byline = full_path
    os.unlink(byline)
    return JsonResponse({"saved": True})
