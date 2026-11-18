# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def format_header(request, path_param):
    snippet = request.path.split('/')[-1]
    reader = make_reader(snippet)
    handshake = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
