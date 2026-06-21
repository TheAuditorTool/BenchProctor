// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18992 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/BenchmarkTest18992", consumes="application/json")
    public void BenchmarkTest18992(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        if (!graphqlVar.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        System.loadLibrary(graphqlVar);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
