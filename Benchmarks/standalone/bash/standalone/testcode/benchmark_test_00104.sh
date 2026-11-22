#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00104() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00104 "$@"
