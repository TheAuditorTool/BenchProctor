// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14662 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest14662.class);

    @GetMapping("/BenchmarkTest14662")
    public void BenchmarkTest14662(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        LOG.info("Action: {}", envValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
