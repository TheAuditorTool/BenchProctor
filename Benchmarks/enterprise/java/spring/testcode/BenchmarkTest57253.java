// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57253 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest57253.class);

    @GetMapping("/BenchmarkTest57253")
    public void BenchmarkTest57253(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(authHeader, "cookie");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
