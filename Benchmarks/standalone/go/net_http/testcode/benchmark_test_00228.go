// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00228(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	var data string
	if len(forwardedIP) > 0 {
		data = forwardedIP
	} else {
		data = "default"
	}
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, boundedVal))
}
