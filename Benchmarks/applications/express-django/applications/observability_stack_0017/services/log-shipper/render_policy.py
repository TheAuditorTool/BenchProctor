# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def render_policy(request):
    note = request.GET.get('id', '')
    cohort = unquote(note)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': cohort})
    return JsonResponse({"saved": True})
