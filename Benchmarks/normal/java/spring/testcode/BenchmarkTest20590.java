// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20590 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest20590")
    public void BenchmarkTest20590(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = trimEnds(originValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
