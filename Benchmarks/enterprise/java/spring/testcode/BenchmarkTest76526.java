// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76526 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest76526.class);

    @GetMapping("/BenchmarkTest76526")
    public void BenchmarkTest76526(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        LOG.info("Action: {}", envValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
