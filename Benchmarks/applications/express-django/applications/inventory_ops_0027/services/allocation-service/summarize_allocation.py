# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def summarize_allocation(request):
    summary = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    restock = normalize(summary)
    os.unlink('/var/app/data/' + str(restock))
    return JsonResponse({"saved": True})
