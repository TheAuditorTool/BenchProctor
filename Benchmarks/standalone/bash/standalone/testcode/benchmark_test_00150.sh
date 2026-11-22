#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00150() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo CAST5 --allow-old-cipher-algos -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00150 "$@"
