// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00002(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	data := strings.ReplaceAll(jsonValue, "\x00", "")
	proc, err := os.StartProcess("/bin/sh", []string{"sh", "-c", "echo " + data}, &os.ProcAttr{Files: []*os.File{nil, os.Stdout, os.Stderr}})
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	procState, err := proc.Wait()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, map[string]string{"exit": strconv.Itoa(procState.ExitCode())})
}
