// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00105(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var data string
	if len(redisValue) > 0 {
		data = redisValue
	} else {
		data = "default"
	}
	lookupStmt, err := DB.Prepare("SELECT id, name FROM users WHERE id = $1")
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query(data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
