// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10131 {

    @GetMapping("/BenchmarkTest10131")
    public void BenchmarkTest10131(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = String.join(" ", refererValue.split("\\s+"));
        response.sendError(500, data);
    }
}
