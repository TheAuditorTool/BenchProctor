// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14712 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest14712")
    public void BenchmarkTest14712(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
