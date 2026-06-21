// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06272 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest06272.class);

    @GetMapping("/BenchmarkTest06272")
    public void BenchmarkTest06272(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!("true".equals(headerValue) || "false".equals(headerValue))) { response.sendError(400); return; }
        LOG.info("Action: {}", headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
