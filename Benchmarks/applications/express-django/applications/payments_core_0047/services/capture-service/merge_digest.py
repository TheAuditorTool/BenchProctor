# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def merge_digest(request):
    footnote = request.GET.get('id', '')
    remittance = unquote(footnote)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': remittance})
    return JsonResponse({"saved": True})
