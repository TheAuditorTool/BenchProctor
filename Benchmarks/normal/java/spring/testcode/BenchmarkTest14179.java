// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14179 {

    private static String stripWhitespace(String v) { return v.strip(); }
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest14179.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @PostMapping("/BenchmarkTest14179")
    public void BenchmarkTest14179(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = stripWhitespace(commentValue);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
