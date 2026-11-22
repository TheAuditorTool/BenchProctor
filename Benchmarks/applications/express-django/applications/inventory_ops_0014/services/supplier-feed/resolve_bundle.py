# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def resolve_bundle(request):
    excerpt = request.GET.get('id', '')
    restock = unquote(excerpt)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': restock})
    return JsonResponse({"saved": True})
