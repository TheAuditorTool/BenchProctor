// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00352 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest00352.class);

    @PostMapping(path="/BenchmarkTest00352", consumes="application/xml")
    public void BenchmarkTest00352(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        byte[] raw = xmlValue.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
