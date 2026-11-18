// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00267(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	var data string
	if len(uploadName) > 0 {
		data = uploadName
	} else {
		data = "default"
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
