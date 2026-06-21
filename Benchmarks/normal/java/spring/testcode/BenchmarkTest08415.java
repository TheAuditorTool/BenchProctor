// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08415 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest08415.class);

    @GetMapping("/BenchmarkTest08415")
    public void BenchmarkTest08415(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String prefix = hostValue.length() > 0 ? hostValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = hostValue.toLowerCase(); break;
            case "f": data = hostValue.toUpperCase(); break;
            default: data = hostValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
