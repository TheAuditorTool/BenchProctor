// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00057(c *gin.Context) {
	pathValue := c.Param("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(pathValue)
	var u User
	if err := gormDB.Where("id = ?", data).First(&u).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
