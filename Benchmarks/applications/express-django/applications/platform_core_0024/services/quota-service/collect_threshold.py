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
def collect_threshold(request):
    heading = os.environ.get('PLATFORM_INPUT_0024', '')
    handshake = RequestPayload(heading).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, handshake))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    persona = full_path
    os.unlink(persona)
    return JsonResponse({"saved": True})
