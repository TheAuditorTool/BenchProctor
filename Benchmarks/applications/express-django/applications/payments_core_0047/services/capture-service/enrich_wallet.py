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
def enrich_wallet(request):
    footnote = os.environ.get('PAYMENTS_INPUT_0047', '')
    remittance = RequestPayload(footnote).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, remittance))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    disbursement = full_path
    os.unlink(disbursement)
    return JsonResponse({"saved": True})
