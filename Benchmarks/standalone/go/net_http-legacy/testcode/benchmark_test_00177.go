// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00177(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	hostValue := r.Host
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(hostValue)
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]interface{}{"display_name": boundedVal, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
