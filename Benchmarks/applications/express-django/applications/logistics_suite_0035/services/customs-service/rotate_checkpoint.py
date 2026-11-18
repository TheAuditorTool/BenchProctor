# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def rotate_checkpoint(request):
    phrase = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(phrase)
    parcel = reader()
    os.unlink('/var/app/data/' + str(parcel))
    return JsonResponse({"saved": True})
