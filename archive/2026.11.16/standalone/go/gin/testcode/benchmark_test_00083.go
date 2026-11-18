// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00083(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
