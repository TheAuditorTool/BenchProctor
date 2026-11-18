// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00025(c *gin.Context) {
	userID := c.Query("id")
	var data string
	if len(userID) > 0 {
		data = userID
	} else {
		data = "default"
	}
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
