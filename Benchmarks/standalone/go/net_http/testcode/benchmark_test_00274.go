// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00274(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := string(bytes.TrimSpace([]byte(rawBody)))
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		http.Error(w, "invalid number", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	directoryFile, openErr := os.Open("/var/app/data/users.xml")
	if openErr != nil {
		http.Error(w, openErr.Error(), http.StatusInternalServerError)
		return
	}
	defer directoryFile.Close()
	xmlDoc, xmlErr := xmlquery.Parse(directoryFile)
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	userNodes, queryErr := xmlquery.QueryAll(xmlDoc, "//user[@name='"+boundedVal+"']")
	if queryErr != nil {
		http.Error(w, "invalid user name", http.StatusBadRequest)
		return
	}
	w.Header().Set("X-User-Matches", strconv.Itoa(len(userNodes)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
