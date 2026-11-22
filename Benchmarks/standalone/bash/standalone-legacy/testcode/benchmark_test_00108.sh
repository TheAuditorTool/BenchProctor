#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00108() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  data="${user_input//$'\x00'/}"
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00108 "$@"
