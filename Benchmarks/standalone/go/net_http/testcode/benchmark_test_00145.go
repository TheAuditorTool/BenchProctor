// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00145(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(uaValue)
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
