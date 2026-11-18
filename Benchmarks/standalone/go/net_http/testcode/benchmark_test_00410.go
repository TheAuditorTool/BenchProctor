// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00410(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	data := func(v string) string { return strings.TrimSpace(v) }(originValue)
	http.Redirect(w, r, data, http.StatusFound)
}
