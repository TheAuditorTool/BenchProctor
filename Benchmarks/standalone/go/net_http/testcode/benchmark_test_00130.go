// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00130(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(w, r)
}
