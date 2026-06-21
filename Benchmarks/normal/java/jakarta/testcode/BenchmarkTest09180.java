// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09180 {

    @GET
    @Path("/BenchmarkTest09180")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09180(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(refererValue);
        String data = carrier.toString();
        return Response.status(500).entity(data).build();
    }
}
