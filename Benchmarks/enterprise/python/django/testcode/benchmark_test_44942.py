# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def to_text(value):
    return str(value).strip()

def BenchmarkTest44942(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
