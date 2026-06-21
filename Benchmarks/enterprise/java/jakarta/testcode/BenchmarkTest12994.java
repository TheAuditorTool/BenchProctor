// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12994 {

    @GET
    @Path("/BenchmarkTest12994")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12994(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + uaValue + "\">", MediaType.TEXT_HTML).build();
    }
}
