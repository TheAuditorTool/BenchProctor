// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00284(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	decodedBytes, _ := base64.StdEncoding.DecodeString(cookieValue)
	data := string(decodedBytes)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
