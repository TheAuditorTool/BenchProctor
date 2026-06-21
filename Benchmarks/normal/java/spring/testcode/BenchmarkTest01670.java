// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01670 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest01670.class);

    @GetMapping("/BenchmarkTest01670")
    public void BenchmarkTest01670(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.function.Function<String, String> tabNormalizer = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(envValue);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
