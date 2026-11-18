// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00234(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	var data string
	if len(pathValue) > 0 {
		data = pathValue
	} else {
		data = "default"
	}
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
