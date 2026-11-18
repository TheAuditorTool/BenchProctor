#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00412() {
  user_input="$HTTP_REFERER"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00412 "$@"
