// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00431(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := func(v string) string { return strings.TrimSpace(v) }(redisValue)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
