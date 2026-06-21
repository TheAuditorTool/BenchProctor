// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest79736 {

    @GET
    @Path("/BenchmarkTest79736")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest79736(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String processed = org.owasp.encoder.Encode.forHtml(hostValue);
        return Response.ok("<div>" + processed + "</div>", MediaType.TEXT_HTML).build();
    }
}
