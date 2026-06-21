// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest53214 {

    @GET
    @Path("/BenchmarkTest53214")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest53214(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        response.addCookie(new Cookie("session", userId));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
