// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00095(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := strings.Join(strings.FieldsFunc(uaValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	query := fmt.Sprintf(`SELECT * FROM "%s"`, strings.ReplaceAll(data, `"`, `""`))
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
