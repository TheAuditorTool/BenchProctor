# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def collect_checkpoint(request):
    paragraph = request.GET.get('id', '')
    gauge = unquote(paragraph)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': gauge})
    return JsonResponse({"saved": True})
