// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00246(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
