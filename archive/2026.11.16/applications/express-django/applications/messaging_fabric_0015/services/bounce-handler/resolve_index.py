# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def resolve_index(request):
    heading = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        bulletin = json.loads(heading).get('value', heading)
    except (json.JSONDecodeError, AttributeError):
        bulletin = heading
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", bulletin):
        return JsonResponse({'error': 'forbidden'}, status=400)
    excerpt = bulletin
    os.unlink('/var/app/data/' + str(excerpt))
    return JsonResponse({"saved": True})
