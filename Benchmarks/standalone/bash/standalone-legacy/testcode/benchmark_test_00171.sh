#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00171() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  case $data in config.json|index.html|readme.md) checked_path="/var/app/data/$data";; *) echo "forbidden"; exit 1;; esac
  rm -f "$checked_path"
}

benchmark_test_00171 "$@"
