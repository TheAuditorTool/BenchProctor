#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00296() {
  user_input="$(amqp-get --url="${AMQP_URL:-amqp://guest:guest@broker:5672/%2F}" --queue=app-events 2>/dev/null)"
  data=$(printf "%b" "$user_input")
  _host=$(echo "$data" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  curl -s "$target_url"
}

benchmark_test_00296 "$@"
