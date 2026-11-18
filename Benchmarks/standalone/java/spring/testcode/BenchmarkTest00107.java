// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00107 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00107", consumes="application/json")
    public void BenchmarkTest00107(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data = graphqlVar.isEmpty() ? "default" : graphqlVar;
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        response.addHeader("Set-Cookie", "session=" + cookieValue + "; Path=/; HttpOnly; SameSite=Strict");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
