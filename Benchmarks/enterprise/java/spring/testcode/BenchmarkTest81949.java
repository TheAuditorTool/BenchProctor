// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81949 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest81949")
    public void BenchmarkTest81949(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
