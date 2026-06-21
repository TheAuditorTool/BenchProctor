// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79947 {

    @PostMapping(path="/BenchmarkTest79947", consumes="text/plain")
    public void BenchmarkTest79947(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = new String(java.util.Base64.getDecoder().decode(rawData));
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
