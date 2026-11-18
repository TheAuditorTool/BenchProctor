// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00084(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	relayPrefix := ""
	if len(uaValue) > 0 {
		relayPrefix = strings.ToLower(uaValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uaValue
	case "f":
		data = uaValue
	default:
		data = uaValue
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
