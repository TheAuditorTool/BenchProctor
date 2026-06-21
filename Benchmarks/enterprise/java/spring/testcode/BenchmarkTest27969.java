// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27969 {

    @PostMapping(path="/BenchmarkTest27969", consumes="text/plain")
    public void BenchmarkTest27969(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = String.format("%s", rawData);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
