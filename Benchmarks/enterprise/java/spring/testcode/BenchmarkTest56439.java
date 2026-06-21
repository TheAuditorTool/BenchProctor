// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56439 {

    @PostMapping("/BenchmarkTest56439")
    public void BenchmarkTest56439(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        byte[] buf = new byte[Integer.parseInt(fieldValue)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
