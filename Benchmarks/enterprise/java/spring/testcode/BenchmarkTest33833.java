// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33833 {

    @PostMapping(path="/BenchmarkTest33833", consumes="application/xml")
    public void BenchmarkTest33833(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder envelope = new StringBuilder();
        envelope.append(xmlValue);
        String data = envelope.toString();
        if (data.length() > 2048) { response.sendError(400, "schema invalid"); return; }
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
