// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00274(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	pending := strings.Split(dbValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		http.Error(w, "invalid boolean", http.StatusBadRequest)
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, parsedBool))
}
