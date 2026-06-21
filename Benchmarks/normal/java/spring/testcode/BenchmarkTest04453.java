// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04453 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest04453", consumes="application/xml")
    public void BenchmarkTest04453(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripWhitespace(xmlValue);
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
