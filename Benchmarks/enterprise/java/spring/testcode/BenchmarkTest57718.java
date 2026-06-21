// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57718 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest57718")
    public void BenchmarkTest57718(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        atomicValue.set(refererValue);
        String data = atomicValue.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            java.util.Hashtable<String,String> env = new java.util.Hashtable<>();
            env.put(javax.naming.Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
            env.put(javax.naming.Context.PROVIDER_URL, "ldap://localhost:389");
            javax.naming.directory.DirContext ctx = new javax.naming.directory.InitialDirContext(env);
            try {
                ctx.search("ou=users,dc=example,dc=com", "(uid=" + data + ")", new javax.naming.directory.SearchControls());
            } finally { ctx.close(); }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
