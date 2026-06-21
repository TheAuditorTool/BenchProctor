// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81649 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/BenchmarkTest81649", consumes="application/json")
    public void BenchmarkTest81649(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + graphqlVar;
        String data = valueSupplier.get();
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
