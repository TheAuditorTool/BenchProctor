// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37023 {

    @GetMapping("/BenchmarkTest37023")
    public void BenchmarkTest37023(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = String.join(" ", refererValue.split("\\s+"));
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
