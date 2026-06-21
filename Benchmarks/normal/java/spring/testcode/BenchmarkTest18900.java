// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18900 {

    @GetMapping("/BenchmarkTest18900")
    public void BenchmarkTest18900(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(uaValue);
        String data = carrier.toString();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
