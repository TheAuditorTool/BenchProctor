// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44414 {

    @PostMapping("/BenchmarkTest44414")
    public void BenchmarkTest44414(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(fieldValue);
        String data = wrapper.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + processed + "\"}");
    }
}
