#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00430() {
  user_input="$HTTP_AUTHORIZATION"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00430 "$@"
