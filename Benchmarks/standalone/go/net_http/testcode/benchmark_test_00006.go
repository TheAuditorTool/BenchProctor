// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00006(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
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
