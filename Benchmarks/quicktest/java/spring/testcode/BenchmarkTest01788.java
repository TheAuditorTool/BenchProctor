// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01788 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest01788.class);

    @GetMapping("/BenchmarkTest01788")
    public void BenchmarkTest01788(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String prefix = envValue.length() > 0 ? envValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = envValue.toLowerCase(); break;
            case "f": data = envValue.toUpperCase(); break;
            default: data = envValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
