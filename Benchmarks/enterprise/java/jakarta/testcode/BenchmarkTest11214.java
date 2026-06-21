// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11214 {

    @GET
    @Path("/BenchmarkTest11214")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11214(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(cookieValue)); }
        catch (NumberFormatException e) { data = cookieValue; }
        java.io.File listingDir = new java.io.File("/var/www/uploads");
        java.io.File[] entries = listingDir.listFiles();
        if (entries != null) {
            for (java.io.File listedFile : entries) {
                response.getWriter().println(listedFile.getName());
            }
        }
        return Response.ok().build();
    }
}
