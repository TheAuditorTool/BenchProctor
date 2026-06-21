// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56731 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/BenchmarkTest56731", consumes="application/json")
    public void BenchmarkTest56731(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(graphqlVar);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            try {
                java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
                java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
                response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
            } catch (Exception e) { response.sendError(502); }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
