// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00077(c *gin.Context) {
	_fileBytes, _ := os.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	var data string
	if len(fileValue) > 0 {
		data = fileValue
	} else {
		data = "default"
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users ORDER BY " + processed).Scan(&matched).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
