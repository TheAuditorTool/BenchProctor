// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33312 {

    @GetMapping("/BenchmarkTest33312")
    public void BenchmarkTest33312(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = refererValue.replace("\u0000", "");
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
