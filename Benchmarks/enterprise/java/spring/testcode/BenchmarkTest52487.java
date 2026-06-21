// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52487 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest52487.class);

    @GetMapping("/BenchmarkTest52487")
    public void BenchmarkTest52487(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(propValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
