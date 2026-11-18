// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
)

func BenchmarkTest00491(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var data string
	if len(uaValue) > 0 {
		data = uaValue
	} else {
		data = "default"
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
