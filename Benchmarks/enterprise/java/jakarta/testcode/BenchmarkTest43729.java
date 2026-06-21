// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43729 {

    @GET
    @Path("/BenchmarkTest43729")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43729(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String prefix = envValue.length() > 0 ? envValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = envValue.toLowerCase(); break;
            case "f": data = envValue.toUpperCase(); break;
            default: data = envValue.strip(); break;
        }
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { return Response.status(400).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
