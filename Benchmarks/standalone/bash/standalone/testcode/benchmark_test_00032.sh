#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00032() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo CAST5 --allow-old-cipher-algos -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00032 "$@"
