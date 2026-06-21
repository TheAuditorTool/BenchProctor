// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest81750 {

    @GET
    @Path("/BenchmarkTest81750")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest81750(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(forwardedIp, "body");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        String processed = org.owasp.encoder.Encode.forHtml(data);
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + processed + "\">", MediaType.TEXT_HTML).build();
    }
}
