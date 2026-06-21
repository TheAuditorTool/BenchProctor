// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68807 {

    @GET
    @Path("/BenchmarkTest68807")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68807(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        request.getSession().setMaxInactiveInterval(900);
        request.getSession().setAttribute("data", String.valueOf(originValue));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
