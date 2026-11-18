# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def reconcile_index(request):
    heading = request.META.get('HTTP_USER_AGENT', '')
    try:
        bulletin = json.loads(heading).get('value', heading)
    except (json.JSONDecodeError, AttributeError):
        bulletin = heading
    with open('/var/app/data/' + str(bulletin), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
