// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00318(c *gin.Context) {
	pathValue := c.Param("id")
	data := strings.ReplaceAll(pathValue, "\x00", "")
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
