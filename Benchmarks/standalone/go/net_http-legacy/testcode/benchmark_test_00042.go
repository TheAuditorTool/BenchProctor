// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00042(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	uaValue := r.Header.Get("User-Agent")
	data := uaValue
	if _, after, ok := strings.Cut(uaValue, ","); ok {
		data = after
	}
	const exportRecordSize = 512
	recordCount, err := strconv.ParseInt(data, 10, 32)
	if err != nil {
		http.Error(w, "invalid record count", http.StatusBadRequest)
		return
	}
	exportBuf := make([]byte, 0, int32(recordCount)*exportRecordSize)
	w.Header().Set("X-Export-Capacity", strconv.Itoa(cap(exportBuf)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
