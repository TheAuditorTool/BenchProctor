#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00015() {
  user_input="`sed -n '/^\r*$/{n;s/\r$//;p;q}'`"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  printf '%s' "$data" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 3 --symmetric --cipher-algo AES256 -o /var/app/run/record.gpg 3<<<"$DATA_ENC_KEY"
}

benchmark_test_00015 "$@"
