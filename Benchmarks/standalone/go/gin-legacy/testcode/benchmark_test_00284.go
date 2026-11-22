// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00284(c *gin.Context) {
	pathValue := c.Param("id")
	var data string
	if pathValue != "" {
		data = pathValue
	}
	resp, err := http.Get(data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
