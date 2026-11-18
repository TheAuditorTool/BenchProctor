// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00062(c *gin.Context) {
	_cfgBytes, _ := os.ReadFile("/etc/app/config.json")
	configValue := string(_cfgBytes)
	data := fmt.Sprintf("%s", configValue)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
