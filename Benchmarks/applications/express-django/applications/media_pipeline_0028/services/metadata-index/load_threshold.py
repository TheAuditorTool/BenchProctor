# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def load_threshold(request):
    citation = request.GET.get('id', '')
    rendition = unquote(citation)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': rendition})
    return JsonResponse({"saved": True})
