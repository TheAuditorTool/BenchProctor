// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00205(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := strings.Join(strings.FieldsFunc(forwardedIP, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]any{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
