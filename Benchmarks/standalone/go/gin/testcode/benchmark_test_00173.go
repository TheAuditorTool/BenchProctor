// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00173(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	data := fmt.Sprintf("%s", jsonValue)
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
