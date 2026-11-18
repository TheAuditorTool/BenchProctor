// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00574(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	pending := strings.Split(forwardedIP, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
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
