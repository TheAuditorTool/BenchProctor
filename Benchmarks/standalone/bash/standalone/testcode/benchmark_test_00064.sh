#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00064() {
  user_input="$HTTP_HOST"
  printf '%s' "$user_input" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00064 "$@"
