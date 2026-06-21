// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11746 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest11746.class);

    @GetMapping("/BenchmarkTest11746")
    public void BenchmarkTest11746(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        LOG.info("Action: {}", hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
