// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71586 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest71586.class);

    @GetMapping("/BenchmarkTest71586")
    public void BenchmarkTest71586(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
