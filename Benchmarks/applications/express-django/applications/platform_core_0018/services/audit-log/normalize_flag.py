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
def normalize_flag(request):
    subtitle = os.environ.get('PLATFORM_INPUT_0018', '')
    persona = RequestPayload(subtitle).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, persona))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    handshake = full_path
    os.unlink(handshake)
    return JsonResponse({"saved": True})
