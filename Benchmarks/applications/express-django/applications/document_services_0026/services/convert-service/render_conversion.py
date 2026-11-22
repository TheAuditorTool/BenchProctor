# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def render_conversion(request):
    preface = request.GET.get('id', '')
    addendum = unquote(preface)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': addendum})
    return JsonResponse({"saved": True})
