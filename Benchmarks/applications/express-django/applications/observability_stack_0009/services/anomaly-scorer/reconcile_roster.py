# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def reconcile_roster(request):
    summary = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(summary).split(',')
    gauge = ' '.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return JsonResponse({"saved": True})
