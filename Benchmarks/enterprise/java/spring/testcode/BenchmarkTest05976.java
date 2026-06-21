// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05976 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest05976", consumes="application/xml")
    public void BenchmarkTest05976(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        response.getWriter().print(data + ",data\n");
    }
}
