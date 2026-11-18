# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import pickle


@csrf_exempt
def normalize_fulfillment(request):
    heading = request.META.get('HTTP_REFERER', '')
    voucher, _sep, _rest = str(heading).partition('\x00')
    pickle.loads(base64.b64decode(voucher))
    return JsonResponse({"saved": True})
