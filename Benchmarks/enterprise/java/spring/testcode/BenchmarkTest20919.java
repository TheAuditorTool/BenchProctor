// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20919 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest20919.class);

    @GetMapping("/BenchmarkTest20919")
    public void BenchmarkTest20919(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String prefix = propValue.length() > 0 ? propValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = propValue.toLowerCase(); break;
            case "f": data = propValue.toUpperCase(); break;
            default: data = propValue.strip(); break;
        }
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
