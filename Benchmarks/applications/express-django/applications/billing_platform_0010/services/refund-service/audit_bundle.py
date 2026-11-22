# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import base64
import pickle


@csrf_exempt
def audit_bundle(request):
    headline = request.POST.get('field', '')
    try:
        remittance = json.loads(headline).get('value', headline)
    except (json.JSONDecodeError, AttributeError):
        remittance = headline
    pickle.loads(base64.b64decode(remittance))
    return JsonResponse({"saved": True})
