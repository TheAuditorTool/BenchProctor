// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00175 {

    @GetMapping("/BenchmarkTest00175")
    public void BenchmarkTest00175(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(headerValue)); }
        catch (NumberFormatException e) { data = headerValue; }
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary";
            case "abort": accessLevel = accessLevel + "+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
