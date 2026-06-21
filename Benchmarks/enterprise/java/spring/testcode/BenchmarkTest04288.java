// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04288 {

    @PostMapping(path="/BenchmarkTest04288", consumes="application/xml")
    public void BenchmarkTest04288(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = "[%s]".formatted(xmlValue);
        byte[] buf = new byte[Integer.parseInt(data)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
