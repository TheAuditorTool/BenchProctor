// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81944 {

    @GetMapping("/BenchmarkTest81944")
    public void BenchmarkTest81944(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = String.format("payload=%s", uaValue);
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(data).find()) {
            response.setHeader("X-Validated-Input", data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
