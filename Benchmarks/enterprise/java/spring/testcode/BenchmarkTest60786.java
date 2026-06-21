// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60786 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest60786")
    public void BenchmarkTest60786(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
