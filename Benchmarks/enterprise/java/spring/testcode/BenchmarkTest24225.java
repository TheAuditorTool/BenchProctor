// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24225 {

    @GetMapping("/BenchmarkTest24225")
    public void BenchmarkTest24225(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(envValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        java.util.Hashtable<String,String> env = new java.util.Hashtable<>();
        env.put(javax.naming.Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(javax.naming.Context.PROVIDER_URL, "ldap://localhost:389");
        javax.naming.directory.DirContext ctx = new javax.naming.directory.InitialDirContext(env);
        try {
            ctx.search("ou=users,dc=example,dc=com", "(uid=" + data + ")", new javax.naming.directory.SearchControls());
        } finally { ctx.close(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
