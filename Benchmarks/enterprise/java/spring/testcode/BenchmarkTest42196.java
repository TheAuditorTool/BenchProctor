// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42196 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest42196")
    public void BenchmarkTest42196(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
