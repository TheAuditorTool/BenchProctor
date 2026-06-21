// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14171 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest14171.class);

    @GetMapping("/BenchmarkTest14171")
    public void BenchmarkTest14171(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
