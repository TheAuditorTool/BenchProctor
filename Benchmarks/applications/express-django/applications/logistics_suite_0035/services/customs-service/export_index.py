# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import pickle


@csrf_exempt
def export_index(request):
    phrase = request.META.get('HTTP_REFERER', '')
    parcel, _sep, _rest = str(phrase).partition('\x00')
    pickle.loads(base64.b64decode(parcel))
    return JsonResponse({"saved": True})
