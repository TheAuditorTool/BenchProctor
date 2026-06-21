// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01390 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest01390.class);

    @GetMapping("/BenchmarkTest01390")
    public void BenchmarkTest01390(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(headerValue);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
