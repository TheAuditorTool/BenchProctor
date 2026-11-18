// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00037(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
