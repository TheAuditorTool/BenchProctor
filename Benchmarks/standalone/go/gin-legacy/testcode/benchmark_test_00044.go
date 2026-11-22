// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00044(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var data string
	if originValue != "" {
		data = originValue
	}
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]interface{}{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
