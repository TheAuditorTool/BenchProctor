#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00057() {
  user_input="$HTTP_REFERER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  xmlstarlet sel -t -v "//user[name='$data']/email" /var/data/users.xml
}

benchmark_test_00057 "$@"
