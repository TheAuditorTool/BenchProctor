// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest36549 {

    @GET
    @Path("/BenchmarkTest36549")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest36549(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("%s", hostValue);
        return Response.ok("{\"resource\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
