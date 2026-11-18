// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
)

func BenchmarkTest00080(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var parsed map[string]interface{}
	json.Unmarshal([]byte(redisValue), &parsed)
	data, _ := parsed["value"].(string)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
