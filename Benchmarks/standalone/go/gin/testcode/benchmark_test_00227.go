// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00227(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	var data string
	if len(rawBody) > 0 {
		data = rawBody
	} else {
		data = "default"
	}
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
