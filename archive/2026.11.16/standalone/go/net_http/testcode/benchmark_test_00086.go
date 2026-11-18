// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00086(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := strings.ReplaceAll(hostValue, "\x00", "")
	http.Redirect(w, r, data, http.StatusFound)
}
