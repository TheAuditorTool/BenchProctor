# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def merge_ledger(request):
    blurb = request.GET.get('id', '')
    inquiry = unquote(blurb)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': inquiry})
    return JsonResponse({"saved": True})
