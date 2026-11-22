// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00054(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", uploadName)
	data := relayBuilder.String()
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
