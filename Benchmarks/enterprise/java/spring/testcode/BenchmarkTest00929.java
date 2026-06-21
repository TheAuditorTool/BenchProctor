// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00929 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest00929.class);

    @GetMapping("/BenchmarkTest00929")
    public void BenchmarkTest00929(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        LOG.info("Action: {}", propValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
