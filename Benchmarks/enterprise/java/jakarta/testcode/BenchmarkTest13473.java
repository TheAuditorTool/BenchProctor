// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest13473 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest13473")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest13473(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        return Response.status(500).entity(data).build();
    }
}
