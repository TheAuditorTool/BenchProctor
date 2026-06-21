// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78619 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest78619")
    public void BenchmarkTest78619(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        response.getWriter().print(String.valueOf(data));
    }
}
