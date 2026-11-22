// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00073(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]interface{}{"display_name": dbValue, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
