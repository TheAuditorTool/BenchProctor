#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00010() {
  user_input="$HTTP_AUTHORIZATION"
  data=`echo "$user_input" | base64 -d 2>/dev/null || echo ""`
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo CAST5 --allow-old-cipher-algos -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00010 "$@"
