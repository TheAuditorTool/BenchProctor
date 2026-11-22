// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
)

func BenchmarkTest00007(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := fmt.Sprintf("%s", hostValue)
	w.Header().Set("Location", data)
	w.WriteHeader(http.StatusSeeOther)
}
