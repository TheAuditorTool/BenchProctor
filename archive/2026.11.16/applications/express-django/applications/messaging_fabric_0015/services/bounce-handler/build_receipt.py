# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def build_receipt(request):
    with open('/etc/app/config.json', 'r') as fh:
        heading = fh.read()
    if heading:
        bulletin = heading
    else:
        bulletin = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return JsonResponse({"saved": True})
