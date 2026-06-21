// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest51994 {

    @GET
    @Path("/BenchmarkTest51994")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest51994(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data;
        if (headerValue.length() > 256) { data = headerValue.substring(0, 256); }
        else { data = headerValue; }
        String normalized = java.text.Normalizer.normalize(data, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        return Response.ok("<p>" + normalized + "</p>", MediaType.TEXT_HTML).build();
    }
}
