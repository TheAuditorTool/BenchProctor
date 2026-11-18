// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00134(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var data string
	if redisValue != "" {
		data = redisValue
	}
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
