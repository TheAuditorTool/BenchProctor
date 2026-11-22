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
def publish_connector(request):
    wording = os.environ.get('INTEGRATIONS_INPUT_0016', '')
    handshake = RequestPayload(wording).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, handshake))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    subject = full_path
    os.unlink(subject)
    return JsonResponse({"saved": True})
