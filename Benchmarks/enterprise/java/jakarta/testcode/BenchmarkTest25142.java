// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25142 {

    @GET
    @Path("/BenchmarkTest25142")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25142(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(hostValue);
        String data = bundle.toString();
        return Response.status(500).entity(data).build();
    }
}
