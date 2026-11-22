// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00171(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	form := submissionForm{payload: redisValue}
	data := form.payload
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
