// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00163(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	var data string
	if len(cookieValue) > 0 {
		data = cookieValue
	} else {
		data = "default"
	}
	http.Redirect(w, r, data, http.StatusFound)
}
