// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00193(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	var data string
	for _, token := range strings.Split(refererValue, ",") {
		data = token
	}
	http.Redirect(w, r, data, http.StatusFound)
}
