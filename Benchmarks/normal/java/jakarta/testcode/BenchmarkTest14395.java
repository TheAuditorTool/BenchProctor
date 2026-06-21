// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14395 {

    @GET
    @Path("/BenchmarkTest14395")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14395(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(refererValue);
        String data = carrier.toString();
        try { Integer.parseInt(data); }
        catch (NumberFormatException e) { return Response.status(400).entity("forbidden").build(); }
        response.addCookie(new Cookie("session", data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
