// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest61527 {

    @PostMapping(path="/BenchmarkTest61527", consumes="application/xml")
    public void BenchmarkTest61527(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        response.getWriter().print(xmlValue + ",data\n");
    }
}
