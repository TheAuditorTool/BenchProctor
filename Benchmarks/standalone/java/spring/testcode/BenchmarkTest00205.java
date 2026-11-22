// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00205 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00205")
    public void BenchmarkTest00205(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", jsonValue);
        String data = holder.getProperty("value", "");
        try (jdk.jshell.JShell snippetShell = jdk.jshell.JShell.builder().executionEngine("local").build()) {
            java.util.List<jdk.jshell.SnippetEvent> snippetEvents = snippetShell.eval(data);
            response.setHeader("X-Code-Result", snippetEvents.isEmpty() ? "" : String.valueOf(snippetEvents.get(0).value()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
