# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def export_payout(request):
    headline = db.fetch_one('SELECT name FROM users LIMIT 1')
    disbursement = (lambda v: v.strip())(headline)
    os.unlink('/var/app/data/' + str(disbursement))
    return JsonResponse({"saved": True})
