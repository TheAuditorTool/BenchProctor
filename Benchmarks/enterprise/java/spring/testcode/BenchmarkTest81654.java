// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81654 {

    @GetMapping("/BenchmarkTest81654")
    public void BenchmarkTest81654(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String prefix = uaValue.length() > 0 ? uaValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uaValue.toLowerCase(); break;
            case "f": data = uaValue.toUpperCase(); break;
            default: data = uaValue.strip(); break;
        }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
