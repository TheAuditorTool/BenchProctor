// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30161 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest30161.class);

    @GetMapping("/BenchmarkTest30161")
    public void BenchmarkTest30161(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        LOG.info("Action: {}", uaValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
