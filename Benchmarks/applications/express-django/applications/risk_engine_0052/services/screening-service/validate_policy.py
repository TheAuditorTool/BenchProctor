# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def validate_policy(request):
    memo = request.GET.get('id', '')
    verdict = unquote(memo)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': verdict})
    return JsonResponse({"saved": True})
