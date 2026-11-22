// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00271(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	var data string
	if len(cookieValue) > 0 {
		data = cookieValue
	} else {
		data = "default"
	}
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]interface{}{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
