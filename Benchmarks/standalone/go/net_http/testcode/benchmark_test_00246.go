// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00246(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	var _num float64
	if _, _err := fmt.Sscanf(uploadName, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, boundedVal))
}
