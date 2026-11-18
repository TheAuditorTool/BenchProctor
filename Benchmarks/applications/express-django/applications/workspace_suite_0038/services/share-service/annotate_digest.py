# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def annotate_digest(request):
    preface = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(preface).split(',')
    remark = ' '.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(remark) + "'")
    return JsonResponse({"saved": True})
