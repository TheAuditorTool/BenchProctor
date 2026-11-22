# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def publish_report(request):
    snippet = request.META.get('HTTP_USER_AGENT', '')
    montage = snippet if snippet else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(montage) + "'")
    return JsonResponse({"saved": True})
