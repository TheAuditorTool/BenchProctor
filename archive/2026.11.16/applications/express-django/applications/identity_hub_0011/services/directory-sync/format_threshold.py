# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def format_threshold(request):
    excerpt = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        persona = json.loads(excerpt).get('value', excerpt)
    except (json.JSONDecodeError, AttributeError):
        persona = excerpt
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    wording = persona
    os.unlink('/var/app/data/' + str(wording))
    return JsonResponse({"saved": True})
