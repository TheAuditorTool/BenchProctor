// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05940 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest05940")
    public void BenchmarkTest05940(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = toLowerCase(refererValue);
        byte[] buf = new byte[Integer.parseInt(data)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
