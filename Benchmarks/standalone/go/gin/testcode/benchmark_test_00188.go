// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00188(c *gin.Context) {
	userID := c.Query("id")
	hexBytes, _ := hex.DecodeString(userID)
	data := string(hexBytes)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9_.#\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	lookupStmt, err := DB.Prepare("SELECT id, name FROM users WHERE name = '" + processed + "'")
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
