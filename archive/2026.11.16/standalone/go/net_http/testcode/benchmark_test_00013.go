// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00013(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
