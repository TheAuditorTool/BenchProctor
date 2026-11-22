// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00038(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(dbValue)
	lookupStmt, err := DB.Prepare("SELECT id, name FROM users WHERE name = '" + data + "'")
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
