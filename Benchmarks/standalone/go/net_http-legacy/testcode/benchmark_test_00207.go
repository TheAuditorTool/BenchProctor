// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00207(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	originValue := r.Header.Get("Origin")
	var data string
	if originValue != "" {
		data = originValue
	}
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]interface{}{"display_name": data, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
