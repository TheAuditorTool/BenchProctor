# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def format_bundle(request):
    synopsis = request.GET.get('id', '')
    byline = unquote(synopsis)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': byline})
    return JsonResponse({"saved": True})
