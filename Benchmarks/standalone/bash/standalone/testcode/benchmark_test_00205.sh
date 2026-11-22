#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00205() {
  user_input="$(amqp-get --url="${AMQP_URL:-amqp://guest:guest@broker:5672/%2F}" --queue=app-events 2>/dev/null)"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  sqlite3 /var/app/data/app.db "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00205 "$@"
