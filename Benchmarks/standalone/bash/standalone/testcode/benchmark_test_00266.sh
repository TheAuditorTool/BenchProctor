#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00266() {
  user_input="$HTTP_ORIGIN"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  case $data in config.json|index.html|readme.md) checked_path="/var/app/data/$data";; *) echo "forbidden"; exit 1;; esac
  cat "$checked_path"
}

benchmark_test_00266 "$@"
