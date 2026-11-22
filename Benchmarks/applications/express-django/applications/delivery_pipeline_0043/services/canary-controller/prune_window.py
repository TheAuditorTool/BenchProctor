# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def prune_window(request):
    remark = request.GET.get('id', '')
    note = unquote(remark)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': note})
    return JsonResponse({"saved": True})
