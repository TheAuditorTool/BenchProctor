# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def resolve_redaction(request):
    snippet = request.GET.get('id', '')
    addendum = unquote(snippet)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': addendum})
    return JsonResponse({"saved": True})
