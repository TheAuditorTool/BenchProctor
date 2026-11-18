# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def load_index(request):
    caption = request.FILES['upload'].name
    cohort = (lambda v: v.strip())(caption)
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return JsonResponse({"saved": True})
