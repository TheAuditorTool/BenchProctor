// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17249 {

    @PostMapping(path="/BenchmarkTest17249", consumes="multipart/form-data")
    public void BenchmarkTest17249(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : multipartValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
