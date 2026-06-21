// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest60007 {

    @GET
    @Path("/BenchmarkTest60007")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest60007(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data;
        if (envValue.length() > 256) { data = envValue.substring(0, 256); }
        else { data = envValue; }
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
