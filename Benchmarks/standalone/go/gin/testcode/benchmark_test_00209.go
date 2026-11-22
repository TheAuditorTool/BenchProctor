// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00209(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	var data string
	if rawBody != "" {
		data = rawBody
	}
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
