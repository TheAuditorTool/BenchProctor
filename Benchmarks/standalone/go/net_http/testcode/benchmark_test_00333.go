// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"regexp"
)

func BenchmarkTest00333(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var data string
	if len(redisValue) > 0 {
		data = redisValue
	} else {
		data = "default"
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9_.#\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", processed)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
