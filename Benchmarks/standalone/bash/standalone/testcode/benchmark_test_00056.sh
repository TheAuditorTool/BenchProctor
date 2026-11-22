#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00056() {
  user_input="$QUERY_STRING"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo CAST5 --allow-old-cipher-algos -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00056 "$@"
