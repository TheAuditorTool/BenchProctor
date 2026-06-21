// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16201 {

    @PostMapping(path="/BenchmarkTest16201", consumes="text/plain")
    public void BenchmarkTest16201(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + rawData + "\">");
    }
}
