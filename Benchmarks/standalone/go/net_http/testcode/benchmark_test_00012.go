// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00012(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(pathValue)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
