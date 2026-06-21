// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest28294 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest28294")
    public void BenchmarkTest28294(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
