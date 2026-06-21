// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21355 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest21355/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21355(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripWhitespace(pathValue);
        if (!data.matches("^[\\w\\s.;|&$`'\\\"_/\\-{}()=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
