// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25374 {

    @GET
    @Path("/BenchmarkTest25374")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25374(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String processed = org.owasp.encoder.Encode.forHtml(headerValue);
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + processed + "\">", MediaType.TEXT_HTML).build();
    }
}
