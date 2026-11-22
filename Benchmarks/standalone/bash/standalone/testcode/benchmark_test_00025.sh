#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00025() {
  user_input="$(cat /dev/stdin)"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00025 "$@"
