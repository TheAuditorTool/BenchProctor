// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04635 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @PostMapping(path="/BenchmarkTest04635", consumes="application/json")
    public void BenchmarkTest04635(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        FormData payload = new FormData(graphqlVar);
        String data = payload.payload;
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
