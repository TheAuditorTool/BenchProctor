// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33849 {

    @GetMapping("/BenchmarkTest33849")
    public void BenchmarkTest33849(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.join(" ", hostValue.split("\\s+"));
        response.getWriter().print("<div>" + data + "</div>");
    }
}
