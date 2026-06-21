// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05050 {

    private static String trimEnds(String v) { return v.trim(); }
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest05050.class);

    @GetMapping("/BenchmarkTest05050")
    public void BenchmarkTest05050(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = trimEnds(uaValue);
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
