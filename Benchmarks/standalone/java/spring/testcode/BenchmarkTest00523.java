// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00523 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00523")
    public void BenchmarkTest00523(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : uaValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        String processed = data.matches("^(admin|user|guest|service)$") ? data : "admin";
        java.util.Hashtable<String,String> env = new java.util.Hashtable<>();
        env.put(javax.naming.Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(javax.naming.Context.PROVIDER_URL, System.getenv().getOrDefault("LDAP_URL", "ldap://directory:1389"));
        javax.naming.directory.DirContext ctx = new javax.naming.directory.InitialDirContext(env);
        try {
            ctx.search("ou=people,dc=example,dc=com", "(uid=" + processed + ")", new javax.naming.directory.SearchControls());
        } finally { ctx.close(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
