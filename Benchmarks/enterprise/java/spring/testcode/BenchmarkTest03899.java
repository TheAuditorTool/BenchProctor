// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03899 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping("/BenchmarkTest03899")
    public void BenchmarkTest03899(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        try { AllowedValue.valueOf(fieldValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { fieldValue = AllowedValue.values()[0].name().toLowerCase(); }
        new ProcessBuilder("python3", "-c", fieldValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
