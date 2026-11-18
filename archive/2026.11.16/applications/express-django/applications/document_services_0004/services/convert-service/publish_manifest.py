# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def publish_manifest(request):
    excerpt = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        dossier = json.loads(excerpt).get('value', excerpt)
    except (json.JSONDecodeError, AttributeError):
        dossier = excerpt
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", dossier):
        return JsonResponse({'error': 'forbidden'}, status=400)
    addendum = dossier
    os.unlink('/var/app/data/' + str(addendum))
    return JsonResponse({"saved": True})
