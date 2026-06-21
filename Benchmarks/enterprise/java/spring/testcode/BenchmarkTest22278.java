// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22278 {

    @GetMapping("/BenchmarkTest22278")
    public void BenchmarkTest22278(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(refererValue);
        String data = envelope.toString();
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
