// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82974 {

    @GET
    @Path("/BenchmarkTest82974")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82974(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = String.format("%s", uaValue);
        response.setContentType("text/html");
        return Response.ok(data, MediaType.TEXT_HTML).build();
    }
}
