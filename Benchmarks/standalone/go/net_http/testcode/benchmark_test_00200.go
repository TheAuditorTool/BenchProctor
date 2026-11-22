// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
)

func BenchmarkTest00200(w http.ResponseWriter, r *http.Request) {
	_fileBytes, _ := os.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	var data string
	if len(fileValue) > 0 {
		data = fileValue
	} else {
		data = "default"
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users ORDER BY " + processed).Scan(&matched).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
