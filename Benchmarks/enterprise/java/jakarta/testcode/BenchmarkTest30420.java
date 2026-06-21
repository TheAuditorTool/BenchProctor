// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest30420 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GET
    @Path("/BenchmarkTest30420")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30420(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = toLowerCase(envValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        java.util.regex.Pattern inputPattern = java.util.regex.Pattern.compile("[a-zA-Z0-9_-]+");
        if (inputPattern.matcher(processed).find()) {
            response.setHeader("X-Validated-Input", processed);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
