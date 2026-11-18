// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00259(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(rawBody), &parsed)
	data, _ := parsed["value"].(string)
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
