// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00042(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	form := submissionForm{payload: xmlBody}
	data := form.payload
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	if result == nil {
		c.String(404, "not found")
		return
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
