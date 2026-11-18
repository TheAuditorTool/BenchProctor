// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00565(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(xmlBody)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid integer", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	requested, _ := strconv.Atoi(boundedVal)
	allocated := requested + 1
	w.Header().Set("X-Alloc-Size", strconv.Itoa(allocated))
}
