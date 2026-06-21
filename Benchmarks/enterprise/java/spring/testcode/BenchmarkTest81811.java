// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81811 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest81811.class);

    @GetMapping("/BenchmarkTest81811")
    public void BenchmarkTest81811(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), authHeader);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
