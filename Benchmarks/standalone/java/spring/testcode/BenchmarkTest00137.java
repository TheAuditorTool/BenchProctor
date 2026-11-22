// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00137 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00137", consumes="application/json")
    public void BenchmarkTest00137(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", graphqlVar);
        String data = sw.toString();
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.#%\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(data)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        java.util.Hashtable<String,String> env = new java.util.Hashtable<>();
        env.put(javax.naming.Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(javax.naming.Context.PROVIDER_URL, System.getenv().getOrDefault("LDAP_URL", "ldap://directory:1389"));
        javax.naming.directory.DirContext ctx = new javax.naming.directory.InitialDirContext(env);
        try {
            javax.naming.NamingEnumeration<javax.naming.NameClassPair> groupEntries = ctx.list("cn=" + data + ",ou=groups,dc=example,dc=com");
            int groupSize = 0;
            while (groupEntries.hasMore()) { groupEntries.next(); groupSize++; }
            response.setHeader("X-Group-Size", String.valueOf(groupSize));
        } finally { ctx.close(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
