// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00166(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	var parsed map[string]interface{}
	json.Unmarshal([]byte(redisValue), &parsed)
	data, _ := parsed["value"].(string)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
