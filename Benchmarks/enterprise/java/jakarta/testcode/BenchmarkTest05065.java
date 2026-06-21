// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest05065 {

    @GET
    @Path("/BenchmarkTest05065")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05065(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + uaValue + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
