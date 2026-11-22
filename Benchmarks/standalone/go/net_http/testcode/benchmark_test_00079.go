// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00079(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(multipartValue)
	http.Redirect(w, r, data, http.StatusFound)
}
