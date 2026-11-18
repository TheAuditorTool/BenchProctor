// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00435(c *gin.Context) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := io.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(apiValue)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
