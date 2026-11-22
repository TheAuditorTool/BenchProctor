// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00032(w http.ResponseWriter, r *http.Request) {
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
	var data string
	if len(uploadName) > 0 {
		data = uploadName
	} else {
		data = "default"
	}
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]interface{}{"display_name": data, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
