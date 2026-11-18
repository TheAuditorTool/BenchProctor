# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def fetch_roster(request):
    citation = request.GET.get('id', '')
    grievance = citation if citation else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': grievance})
    return JsonResponse({"saved": True})
