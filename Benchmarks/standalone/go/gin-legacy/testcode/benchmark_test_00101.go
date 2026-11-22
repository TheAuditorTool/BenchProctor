// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00101(c *gin.Context) {
	rawBytes, err := ioutil.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	form := submissionForm{payload: rawBody}
	data := form.payload
	c.Set("data", data)
}
