// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00254(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := strings.Join(strings.FieldsFunc(redisValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE name = '" + data + "'").Scan(&matched).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
