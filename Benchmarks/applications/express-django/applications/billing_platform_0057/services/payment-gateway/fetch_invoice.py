# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def fetch_invoice(request):
    caption = request.GET.get('id', '')
    remittance = unquote(caption)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': remittance})
    return JsonResponse({"saved": True})
