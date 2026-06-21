# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest03888(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
