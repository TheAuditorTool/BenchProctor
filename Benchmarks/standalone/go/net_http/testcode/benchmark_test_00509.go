// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
)

func BenchmarkTest00509(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(dbValue), &parsed)
	data, _ := parsed["value"].(string)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
