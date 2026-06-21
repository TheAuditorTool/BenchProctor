// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14070 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @PostMapping(path="/BenchmarkTest14070", consumes="application/json")
    public void BenchmarkTest14070(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Properties holder = new java.util.Properties();
        holder.load(new java.io.StringReader("rawValue=" + graphqlVar.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", holder.getProperty("format", "plain"));
        String data = holder.getProperty("rawValue", "");
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
