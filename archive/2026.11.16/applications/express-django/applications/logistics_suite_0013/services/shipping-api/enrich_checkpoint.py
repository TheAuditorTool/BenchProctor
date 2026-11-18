# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def enrich_checkpoint(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        parcel = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        parcel = footnote
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", parcel):
        return JsonResponse({'error': 'forbidden'}, status=400)
    consignment = parcel
    os.unlink('/var/app/data/' + str(consignment))
    return JsonResponse({"saved": True})
