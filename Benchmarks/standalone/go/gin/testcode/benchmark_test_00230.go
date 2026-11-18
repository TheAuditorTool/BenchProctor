// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00230(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(dbValue), &parsed)
	data, _ := parsed["value"].(string)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
