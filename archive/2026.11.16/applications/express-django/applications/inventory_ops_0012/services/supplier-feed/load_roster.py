# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def load_roster(request):
    phrase = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        backorder = json.loads(phrase).get('value', phrase)
    except (json.JSONDecodeError, AttributeError):
        backorder = phrase
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", backorder):
        return JsonResponse({'error': 'forbidden'}, status=400)
    restock = backorder
    os.unlink('/var/app/data/' + str(restock))
    return JsonResponse({"saved": True})
