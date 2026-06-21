// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34589 {

    @PostMapping(path="/BenchmarkTest34589", consumes="application/xml")
    public void BenchmarkTest34589(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("%s", xmlValue);
        response.sendError(500, data);
    }
}
