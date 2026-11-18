# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def annotate_report(request):
    subject = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(subject).split(',')
    bulletin = ' '.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return JsonResponse({"saved": True})
