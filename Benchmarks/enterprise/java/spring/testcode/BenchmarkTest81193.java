// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81193 {

    @GetMapping("/BenchmarkTest81193")
    public void BenchmarkTest81193(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(userId).find()) {
            response.setHeader("X-Validated-Input", userId);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
