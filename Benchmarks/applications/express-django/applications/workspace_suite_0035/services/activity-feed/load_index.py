# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def load_index(request):
    paragraph = request.META.get('HTTP_USER_AGENT', '')
    wording = paragraph if paragraph else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(wording) + "'")
    return JsonResponse({"saved": True})
