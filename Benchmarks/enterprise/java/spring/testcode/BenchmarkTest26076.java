// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26076 {

    @GetMapping("/BenchmarkTest26076")
    public void BenchmarkTest26076(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!("true".equals(headerValue) || "false".equals(headerValue))) { response.sendError(400); return; }
        request.getSession().setAttribute("data", String.valueOf(headerValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
