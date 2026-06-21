# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest50898(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    return redirect(str(data))
