// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00224(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	hexBytes, _ := hex.DecodeString(headerValue)
	data := string(hexBytes)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
