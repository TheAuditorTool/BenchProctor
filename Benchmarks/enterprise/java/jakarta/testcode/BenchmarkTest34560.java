// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest34560 {

    @GET
    @Path("/BenchmarkTest34560")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest34560(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + hostValue + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
