// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35432 {

    @PostMapping(path="/BenchmarkTest35432", consumes="text/plain")
    public void BenchmarkTest35432(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(rawData);
        String data = bundle.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
        }
    }
}
