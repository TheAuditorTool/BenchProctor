// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24568 {

    @PostMapping("/BenchmarkTest24568")
    public void BenchmarkTest24568(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        byte[] buf = new byte[Integer.parseInt(fieldValue)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
