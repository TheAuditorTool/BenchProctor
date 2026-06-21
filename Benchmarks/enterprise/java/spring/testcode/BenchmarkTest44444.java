// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44444 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest44444")
    public void BenchmarkTest44444(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = expandTabs(headerValue);
        if (!data.matches("^[\\w\\s./\\\\:_?&=\\-@]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
