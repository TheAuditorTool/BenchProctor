# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def collect_schedule(request):
    citation = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(citation).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            backorder = str(citation).strip()
        case _:
            backorder = str(citation)
    requests.get(str(backorder))
    return JsonResponse({"saved": True})
