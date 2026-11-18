// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00383(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	var data string
	for _, token := range strings.Split(headerValue, ",") {
		data = token
	}
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
