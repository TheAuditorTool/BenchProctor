# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def prune_metric(request):
    preface = request.GET.get('id', '')
    cohort = preface if preface else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': cohort})
    return JsonResponse({"saved": True})
