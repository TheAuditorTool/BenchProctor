// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03838 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03838.class);

    @GetMapping("/BenchmarkTest03838")
    public void BenchmarkTest03838(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = headerValue.replace("\u0000", "");
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
