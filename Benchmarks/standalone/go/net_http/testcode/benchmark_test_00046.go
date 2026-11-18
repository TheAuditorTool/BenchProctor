// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00046(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", userID)
	data := relayBuilder.String()
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, boundedVal))
}
