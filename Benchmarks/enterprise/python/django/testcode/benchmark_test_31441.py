# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31441(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
