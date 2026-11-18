// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00363(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9_.#\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", processed)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
