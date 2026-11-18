// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00287(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	data := func(v string) string { return strings.TrimSpace(v) }(authHeader)
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, boundedVal))
}
