#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00404() {
  user_input="$(redis-cli GET user_data)"
  _host=$(echo "$user_input" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$user_input"
  _rest="${target_url#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00404 "$@"
