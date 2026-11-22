// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00074 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00074")
    public void BenchmarkTest00074(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String data = transform.apply(hostValue);
        class SchemaInput {
            @javax.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.#%\\-]+$") final String value;
            SchemaInput(String value) { this.value = value; }
        }
        javax.validation.Validator schemaValidator = javax.validation.Validation.buildDefaultValidatorFactory().getValidator();
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
