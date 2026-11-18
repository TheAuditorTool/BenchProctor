// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00269(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := func(v string) string { return strings.TrimSpace(v) }(redisValue)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
