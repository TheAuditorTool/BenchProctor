// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest17641 {

    @GET
    @Path("/BenchmarkTest17641")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest17641(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String processed = org.owasp.encoder.Encode.forHtml(forwardedIp);
        return Response.ok("<div>" + processed + "</div>", MediaType.TEXT_HTML).build();
    }
}
