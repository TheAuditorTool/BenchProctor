// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00243(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(uploadName)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
