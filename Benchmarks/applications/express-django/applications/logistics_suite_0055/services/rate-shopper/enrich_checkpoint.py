# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def enrich_checkpoint(request, path_param):
    heading = request.path.split('/')[-1]
    reader = make_reader(heading)
    consignment = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(consignment) + "'")
    return JsonResponse({"saved": True})
