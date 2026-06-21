// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26748 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest26748.class);

    @GetMapping("/BenchmarkTest26748")
    public void BenchmarkTest26748(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(userId, "header");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
