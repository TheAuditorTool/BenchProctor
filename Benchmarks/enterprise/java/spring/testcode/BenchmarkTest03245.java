// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03245 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03245.class);

    @GetMapping("/BenchmarkTest03245")
    public void BenchmarkTest03245(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::trim);
        String data = decorated.apply(userId);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        LOG.info("Action: {}", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
