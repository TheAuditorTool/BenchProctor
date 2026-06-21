// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44157 {

    @GET
    @Path("/BenchmarkTest44157")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44157(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String processed = org.owasp.encoder.Encode.forHtml(originValue);
        return Response.ok("<div>" + processed + "</div>", MediaType.TEXT_HTML).build();
    }
}
