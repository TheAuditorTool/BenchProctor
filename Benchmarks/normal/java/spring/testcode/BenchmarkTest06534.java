// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06534 {

    @PostMapping("/BenchmarkTest06534")
    public void BenchmarkTest06534(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(fieldValue).find()) {
            response.setHeader("X-Validated-Input", fieldValue);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
