// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00192(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var data string
	if len(redisValue) > 0 {
		data = redisValue
	} else {
		data = "default"
	}
	lookupStmt, err := DB.Prepare("SELECT id, name FROM users WHERE id = $1")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
