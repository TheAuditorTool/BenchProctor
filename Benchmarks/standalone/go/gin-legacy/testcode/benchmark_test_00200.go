// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00200(c *gin.Context) {
	pathValue := c.Param("id")
	data, _ := url.QueryUnescape(pathValue)
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE name = '" + data + "'").Scan(&matched).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
