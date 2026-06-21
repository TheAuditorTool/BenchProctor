// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77596 {

    private static String trimEnds(String v) { return v.trim(); }

    @PostMapping("/BenchmarkTest77596")
    public void BenchmarkTest77596(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = trimEnds(fieldValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
