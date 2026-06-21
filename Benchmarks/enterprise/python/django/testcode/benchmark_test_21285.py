# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest21285(request):
    stdin_value = input('input: ')
    data = FormData(payload=stdin_value).payload
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
