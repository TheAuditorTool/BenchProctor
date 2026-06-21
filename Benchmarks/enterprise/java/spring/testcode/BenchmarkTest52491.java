// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52491 {

    @GetMapping("/BenchmarkTest52491")
    public void BenchmarkTest52491(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(authHeader).find()) {
            response.setHeader("X-Validated-Input", authHeader);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
