// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00154 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest00154")
    public void BenchmarkTest00154(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        String data = normalize(envValue);
        try (jdk.jshell.JShell snippetShell = jdk.jshell.JShell.builder().executionEngine("local").build()) {
            java.util.List<jdk.jshell.SnippetEvent> snippetEvents = snippetShell.eval(data);
            response.setHeader("X-Code-Result", snippetEvents.isEmpty() ? "" : String.valueOf(snippetEvents.get(0).value()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
