// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00571(c *gin.Context) {
	_fileBytes, _ := os.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	hexBytes, _ := hex.DecodeString(fileValue)
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
