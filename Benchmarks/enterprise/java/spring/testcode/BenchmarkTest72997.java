// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72997 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest72997.class);

    @GetMapping("/BenchmarkTest72997")
    public void BenchmarkTest72997(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::trim);
        String data = composed.apply(propValue);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
