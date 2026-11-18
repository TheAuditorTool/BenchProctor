# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def rotate_manifest(request):
    excerpt = request.GET.get('id', '')
    persona = excerpt if excerpt else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': persona})
    return JsonResponse({"saved": True})
