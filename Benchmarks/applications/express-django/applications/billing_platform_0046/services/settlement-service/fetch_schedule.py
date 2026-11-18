# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def fetch_schedule(request):
    with open('/tmp/data', 'r') as fh:
        remark = fh.read()
    reader = make_reader(remark)
    remittance = reader()
    db.execute('SELECT * FROM "' + str(remittance).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
