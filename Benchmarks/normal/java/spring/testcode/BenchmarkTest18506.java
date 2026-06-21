// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18506 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest18506.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @GetMapping("/BenchmarkTest18506")
    public void BenchmarkTest18506(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try { AllowedValue.valueOf(headerValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { headerValue = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
