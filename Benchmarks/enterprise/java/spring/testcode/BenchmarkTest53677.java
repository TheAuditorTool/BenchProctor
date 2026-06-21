// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53677 {

    @PostMapping("/BenchmarkTest53677")
    public void BenchmarkTest53677(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = fieldValue.replace("\u0000", "");
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(data).find()) {
            response.setHeader("X-Validated-Input", data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
