#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00038() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  case $data in config.json|index.html|readme.md) checked_path="/var/app/data/$data";; *) echo "forbidden"; exit 1;; esac
  rm -f "$checked_path"
}

benchmark_test_00038 "$@"
