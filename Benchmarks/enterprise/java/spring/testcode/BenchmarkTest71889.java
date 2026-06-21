// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71889 {

    @PostMapping("/BenchmarkTest71889")
    public void BenchmarkTest71889(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(fieldValue);
        String data = wrapper.toString();
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
