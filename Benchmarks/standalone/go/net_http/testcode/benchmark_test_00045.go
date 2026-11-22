// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00045(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	data := fmt.Sprintf("%s", uploadName)
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
