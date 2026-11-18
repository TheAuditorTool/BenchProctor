// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strings"
)

func BenchmarkTest00007(w http.ResponseWriter, r *http.Request) {
	var profileBio string
	DB.QueryRow("SELECT bio FROM profiles LIMIT 1").Scan(&profileBio)
	data := strings.ReplaceAll(profileBio, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	content, err := os.ReadFile("/var/app/data/" + processed)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
