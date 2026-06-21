// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46822 {

    @GetMapping("/BenchmarkTest46822")
    public void BenchmarkTest46822(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        byte[] buf = new byte[Integer.parseInt(uaValue)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
