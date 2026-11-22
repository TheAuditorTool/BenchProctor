// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00203(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := strings.Join(strings.FieldsFunc(redisValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE name = '" + data + "'").Scan(&matched).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
