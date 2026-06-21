// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60762 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest60762", consumes="application/xml")
    public void BenchmarkTest60762(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
