// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha3"
	"encoding/hex"
	"net/http"
)

func BenchmarkTest00043(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	form := submissionForm{payload: originValue}
	data := form.payload
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
