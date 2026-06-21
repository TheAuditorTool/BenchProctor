// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09820 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest09820.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @PostMapping("/BenchmarkTest09820")
    public void BenchmarkTest09820(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = String.join(" ", commentValue.split("\\s+"));
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
