# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def prune_threshold(request):
    with open('/etc/app/config.json', 'r') as fh:
        citation = fh.read()
    if citation:
        grievance = citation
    else:
        grievance = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return JsonResponse({"saved": True})
