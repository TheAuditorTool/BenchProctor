// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00243(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(rawBody)
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE name = '" + data + "'").Scan(&matched).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
