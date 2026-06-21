// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10802 {

    @PostMapping(path="/BenchmarkTest10802", consumes="application/xml")
    public void BenchmarkTest10802(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        response.getWriter().print(String.valueOf(xmlValue));
    }
}
