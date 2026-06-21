// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78574 {

    private static String trimEnds(String v) { return v.trim(); }
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest78574.class);

    @GetMapping("/BenchmarkTest78574")
    public void BenchmarkTest78574(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = trimEnds(forwardedIp);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
