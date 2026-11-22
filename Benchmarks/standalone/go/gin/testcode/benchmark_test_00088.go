// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00088(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]any{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
