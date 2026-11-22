// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00038(c *gin.Context) {
	_fileBytes, _ := ioutil.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	decodedBytes, _ := base64.StdEncoding.DecodeString(fileValue)
	data := string(decodedBytes)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
