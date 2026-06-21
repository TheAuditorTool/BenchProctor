// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01492 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest01492")
    public void BenchmarkTest01492(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        response.sendError(500, data);
    }
}
