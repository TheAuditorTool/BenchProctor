// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00216(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]any{"display_name": data, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
