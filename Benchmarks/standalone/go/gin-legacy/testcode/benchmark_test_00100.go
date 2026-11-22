// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00100(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := headerValue
	if _, after, ok := strings.Cut(headerValue, ","); ok {
		data = after
	}
	dialURL, dialErr := url.Parse(data)
	if dialErr != nil {
		c.String(http.StatusBadRequest, "invalid url")
		return
	}
	conn, err := net.Dial("tcp", net.JoinHostPort(dialURL.Hostname(), "80"))
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
