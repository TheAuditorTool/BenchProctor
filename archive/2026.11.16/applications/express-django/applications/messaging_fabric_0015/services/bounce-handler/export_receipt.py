# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def export_receipt(request):
    heading = request.GET.get('id', '')
    bulletin = heading if heading else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': bulletin})
    return JsonResponse({"saved": True})
