// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00289(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	segments := strings.Split(rawBody, ",")
	data := strings.Join(segments, " ")
	trustedSettings.Store("partner_callback_host", data)
	c.JSON(200, gin.H{"code": "OK"})
}
