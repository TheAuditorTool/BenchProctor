// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00182 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00182")
    public void BenchmarkTest00182(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(hostValue)); }
        catch (NumberFormatException e) { data = hostValue; }
        try (jdk.jshell.JShell snippetShell = jdk.jshell.JShell.builder().executionEngine("local").build()) {
            java.util.List<jdk.jshell.SnippetEvent> snippetEvents = snippetShell.eval(data);
            response.setHeader("X-Code-Result", snippetEvents.isEmpty() ? "" : String.valueOf(snippetEvents.get(0).value()));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
