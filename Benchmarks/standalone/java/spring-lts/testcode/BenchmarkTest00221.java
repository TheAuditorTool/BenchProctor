// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00221 {
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

    @PostMapping(path="/BenchmarkTest00221", consumes="application/json")
    public void BenchmarkTest00221(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", graphqlVar);
        String data = container.getProperty("value", "");
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        org.springframework.http.ResponseCookie sessionCookie = org.springframework.http.ResponseCookie.from("session", cookieValue).path("/").httpOnly(true).sameSite("Strict").build();
        response.addHeader(org.springframework.http.HttpHeaders.SET_COOKIE, sessionCookie.toString());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
