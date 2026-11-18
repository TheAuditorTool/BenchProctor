// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
)

func BenchmarkTest00129(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(fieldValue)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#~\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
