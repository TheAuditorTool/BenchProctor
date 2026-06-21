// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63069 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @PostMapping("/BenchmarkTest63069")
    public void BenchmarkTest63069(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        try { AllowedValue.valueOf(jsonValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { jsonValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", jsonValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
