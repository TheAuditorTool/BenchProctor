// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00171(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	pending := strings.Split(hostValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	http.Redirect(w, r, data, http.StatusFound)
}
