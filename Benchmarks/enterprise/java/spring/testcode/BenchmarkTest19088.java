// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19088 {

    @PostMapping("/BenchmarkTest19088")
    public void BenchmarkTest19088(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = String.format("%s", fieldValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
