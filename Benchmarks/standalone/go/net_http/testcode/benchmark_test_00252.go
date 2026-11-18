// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00252(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	segments := strings.Split(uaValue, ",")
	data := strings.Join(segments, " ")
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
