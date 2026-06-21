// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32203 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private static String stripWhitespace(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest32203", consumes="application/json")
    public void BenchmarkTest32203(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data = stripWhitespace(graphqlVar);
        if (data == null) throw new IllegalArgumentException("input required");
        io.github.jopenlibs.vault.VaultConfig vc = new io.github.jopenlibs.vault.VaultConfig()
            .address("https://vault.svc.local:8200")
            .token(System.getenv("VAULT_TOKEN"))
            .build();
        io.github.jopenlibs.vault.Vault vault = io.github.jopenlibs.vault.Vault.create(vc);
        String storeCred = vault.logical().read("secret/myapp/db_password").getData().get("password");
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
