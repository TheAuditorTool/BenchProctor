# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def render_header(request):
    headline = request.GET.get('id', '')
    backorder = unquote(headline)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': backorder})
    return JsonResponse({"saved": True})
