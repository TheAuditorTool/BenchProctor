// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11598 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest11598")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11598(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        return Response.status(500).entity(data).build();
    }
}
