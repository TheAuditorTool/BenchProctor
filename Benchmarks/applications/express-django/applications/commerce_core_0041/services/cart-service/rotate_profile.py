# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def rotate_profile(request):
    headline = request.META.get('HTTP_USER_AGENT', '')
    backorder = headline if headline else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(backorder) + "'")
    return JsonResponse({"saved": True})
