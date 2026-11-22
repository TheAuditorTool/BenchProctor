// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00214(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]interface{}{"display_name": dbValue, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
