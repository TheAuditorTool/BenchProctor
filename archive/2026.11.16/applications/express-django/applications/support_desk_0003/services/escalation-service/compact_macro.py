# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def compact_macro(request):
    citation = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        grievance = json.loads(citation).get('value', citation)
    except (json.JSONDecodeError, AttributeError):
        grievance = citation
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", grievance):
        return JsonResponse({'error': 'forbidden'}, status=400)
    inquiry = grievance
    os.unlink('/var/app/data/' + str(inquiry))
    return JsonResponse({"saved": True})
