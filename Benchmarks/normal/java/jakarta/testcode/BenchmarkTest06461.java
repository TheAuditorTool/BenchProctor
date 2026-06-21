// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06461 {

    @GET
    @Path("/BenchmarkTest06461")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06461(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::trim);
        String data = fullPipeline.apply(refererValue);
        try { Double.parseDouble(data); }
        catch (NumberFormatException e) { return Response.status(400).entity("forbidden").build(); }
        response.addCookie(new Cookie("session", data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
