// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17354 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping(path="/BenchmarkTest17354", consumes="application/json")
    public void BenchmarkTest17354(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data = expandTabs(graphqlVar);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
