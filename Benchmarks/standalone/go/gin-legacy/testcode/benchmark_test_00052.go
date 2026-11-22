// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00052(c *gin.Context) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := ioutil.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", apiValue)
	data := relayBuilder.String()
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
