// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00429(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := fmt.Sprintf("%s", cookieValue)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
