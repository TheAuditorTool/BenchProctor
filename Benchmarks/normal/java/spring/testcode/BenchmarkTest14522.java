// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14522 {

    @PostMapping(path="/BenchmarkTest14522", consumes="application/xml")
    public void BenchmarkTest14522(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data;
        if (xmlValue.length() > 256) { data = xmlValue.substring(0, 256); }
        else { data = xmlValue; }
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
