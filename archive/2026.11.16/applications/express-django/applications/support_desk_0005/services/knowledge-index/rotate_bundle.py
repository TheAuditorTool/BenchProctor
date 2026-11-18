# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def rotate_bundle(request):
    phrase = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        inquiry = json.loads(phrase).get('value', phrase)
    except (json.JSONDecodeError, AttributeError):
        inquiry = phrase
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", inquiry):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = inquiry
    os.unlink('/var/app/data/' + str(grievance))
    return JsonResponse({"saved": True})
