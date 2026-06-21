// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82386 {

    @PostMapping(path="/BenchmarkTest82386", consumes="application/xml")
    public void BenchmarkTest82386(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.isEmpty() ? "default" : xmlValue;
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
