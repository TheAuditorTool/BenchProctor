// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest22862 {

    @GET
    @Path("/BenchmarkTest22862")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22862(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = "" + uaValue;
        response.addCookie(new Cookie("session", data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
