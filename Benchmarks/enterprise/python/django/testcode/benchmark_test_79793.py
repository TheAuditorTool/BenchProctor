# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest79793(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
