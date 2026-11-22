// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00236(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid integer", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	const exportRecordSize = 512
	const maxExportRecords = 10000
	recordCount, err := strconv.ParseInt(boundedVal, 10, 64)
	if err != nil || recordCount < 1 || recordCount > maxExportRecords {
		http.Error(w, "invalid record count", http.StatusBadRequest)
		return
	}
	exportBuf := make([]byte, 0, recordCount*exportRecordSize)
	w.Header().Set("X-Export-Capacity", strconv.Itoa(cap(exportBuf)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
