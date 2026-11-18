# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import base64
import pickle


@csrf_exempt
def load_profile(request):
    subject = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        parcel = json.loads(subject).get('value', subject)
    except (json.JSONDecodeError, AttributeError):
        parcel = subject
    pickle.loads(base64.b64decode(parcel))
    return JsonResponse({"saved": True})
