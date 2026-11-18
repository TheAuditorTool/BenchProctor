// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00037(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(pathValue)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
