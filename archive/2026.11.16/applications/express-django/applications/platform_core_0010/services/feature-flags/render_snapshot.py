# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def render_snapshot(request):
    notice = request.META.get('HTTP_USER_AGENT', '')
    try:
        persona = json.loads(notice).get('value', notice)
    except (json.JSONDecodeError, AttributeError):
        persona = notice
    with open('/var/app/data/' + str(persona), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
