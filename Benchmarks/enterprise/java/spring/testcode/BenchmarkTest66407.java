// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66407 {

    @PostMapping(path="/BenchmarkTest66407", consumes="application/xml")
    public void BenchmarkTest66407(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
