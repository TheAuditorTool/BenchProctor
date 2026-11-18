# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def audit_digest(request):
    excerpt = request.FILES['upload'].name
    gauge = (lambda v: v.strip())(excerpt)
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return JsonResponse({"saved": True})
