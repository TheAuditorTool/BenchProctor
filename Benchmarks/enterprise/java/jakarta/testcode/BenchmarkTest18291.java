// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18291 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest18291")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18291(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        return Response.status(500).entity(data).build();
    }
}
