// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00310(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(authHeader)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
