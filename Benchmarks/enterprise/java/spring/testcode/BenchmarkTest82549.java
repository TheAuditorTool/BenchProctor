// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82549 {

    @GetMapping("/BenchmarkTest82549")
    public void BenchmarkTest82549(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = "[%s]".formatted(uaValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
