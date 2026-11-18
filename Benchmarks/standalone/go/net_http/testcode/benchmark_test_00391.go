// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
)

func BenchmarkTest00391(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	form := submissionForm{payload: dbValue}
	data := form.payload
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	os.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
