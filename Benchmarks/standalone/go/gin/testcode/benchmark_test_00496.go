// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00496(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := strings.Join(strings.FieldsFunc(graphqlVar, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
