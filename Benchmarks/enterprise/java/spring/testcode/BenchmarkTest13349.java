// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13349 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest13349")
    public void BenchmarkTest13349(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
