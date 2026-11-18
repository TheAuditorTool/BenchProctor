// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/go-ldap/ldap/v3"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00273(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(headerValue, "schema"); err != nil {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := headerValue
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		c.String(http.StatusInternalServerError, ldapErr.Error())
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+processed+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		c.Header("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	c.JSON(200, gin.H{"code": "OK"})
}
