# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def audit_threshold(request):
    preface = request.META.get('HTTP_USER_AGENT', '')
    grievance = preface if preface else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return JsonResponse({"saved": True})
