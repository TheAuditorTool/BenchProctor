# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import base64
import pickle


@csrf_exempt
def fetch_profile(request):
    quotation = request.POST.get('field', '')
    try:
        parcel = json.loads(quotation).get('value', quotation)
    except (json.JSONDecodeError, AttributeError):
        parcel = quotation
    pickle.loads(base64.b64decode(parcel))
    return JsonResponse({"saved": True})
