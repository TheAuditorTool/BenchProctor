# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def export_policy(request):
    subtitle = request.GET.get('id', '')
    ledger = subtitle if subtitle else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': ledger})
    return JsonResponse({"saved": True})
