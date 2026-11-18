# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def compact_window(request):
    footnote = request.META.get('HTTP_USER_AGENT', '')
    try:
        parcel = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        parcel = footnote
    with open('/var/app/data/' + str(parcel), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
