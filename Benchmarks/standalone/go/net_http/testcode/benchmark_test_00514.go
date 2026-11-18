// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00514(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	data := strings.Join(strings.FieldsFunc(forwardedIP, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
