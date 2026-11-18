// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00382(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
