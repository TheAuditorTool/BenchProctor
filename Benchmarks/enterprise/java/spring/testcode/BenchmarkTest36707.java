// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36707 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest36707.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @PostMapping("/BenchmarkTest36707")
    public void BenchmarkTest36707(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        try { AllowedValue.valueOf(jsonValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { jsonValue = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", jsonValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
