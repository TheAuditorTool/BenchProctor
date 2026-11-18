// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00580(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	for _, token := range strings.Split(userID, ",") {
		data = token
	}
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
