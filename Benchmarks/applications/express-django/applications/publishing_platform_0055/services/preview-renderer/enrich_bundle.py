# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def enrich_bundle(request):
    synopsis = request.META.get('HTTP_USER_AGENT', '')
    byline = synopsis if synopsis else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(byline) + "'")
    return JsonResponse({"saved": True})
