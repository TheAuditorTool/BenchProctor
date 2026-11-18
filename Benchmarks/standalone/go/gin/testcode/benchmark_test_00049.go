// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os/exec"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00049(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	var data string
	if len(jsonValue) > 0 {
		data = jsonValue
	} else {
		data = "default"
	}
	cmd := exec.Command("python3", "-c", data)
	output, _ := cmd.CombinedOutput()
	c.Data(200, "text/plain", output)
}
