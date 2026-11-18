// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00059(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	decodedBytes, _ := base64.StdEncoding.DecodeString(rawBody)
	data := string(decodedBytes)
	c.Redirect(http.StatusFound, data)
}
