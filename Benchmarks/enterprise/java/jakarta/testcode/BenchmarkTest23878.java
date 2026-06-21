// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest23878 {

    @GET
    @Path("/BenchmarkTest23878")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23878(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.net.URLDecoder.decode(userId, "UTF-8");
        request.getSession().setAttribute("data", String.valueOf(data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
