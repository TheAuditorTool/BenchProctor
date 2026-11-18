// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00080(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
