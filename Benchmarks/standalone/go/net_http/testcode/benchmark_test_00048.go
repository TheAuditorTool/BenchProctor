// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"strconv"
)

func BenchmarkTest00048(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data, _ := url.QueryUnescape(userID)
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	trustedSettings.Store("partner_callback_host", boundedVal)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
