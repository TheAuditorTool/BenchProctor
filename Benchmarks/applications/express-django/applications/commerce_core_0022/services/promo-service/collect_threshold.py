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
    subject = os.environ.get('ORDERS_INPUT_0022', '')
    voucher = RequestPayload(subject).value
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, voucher))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = full_path
    os.unlink(backorder)
    return JsonResponse({"saved": True})
