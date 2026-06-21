// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02873 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest02873")
    public void BenchmarkTest02873(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = stripCRLF(refererValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Access-Control-Allow-Origin", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
