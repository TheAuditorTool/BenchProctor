// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11830 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest11830.class);

    @GetMapping("/BenchmarkTest11830")
    public void BenchmarkTest11830(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(hostValue, "body");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
