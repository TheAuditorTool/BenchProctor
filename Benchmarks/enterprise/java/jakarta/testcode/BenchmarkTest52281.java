// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest52281 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @POST
    @Path("/BenchmarkTest52281")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest52281(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.List<String> tokens = java.util.Arrays.asList(fieldValue.split(","));
        String data = String.join(",", tokens);
        synchronized(SHARED_WRITE_LOCK) {
            sharedLastValue = data;
            int seen = sharedWriteCount;
            sharedWriteCount = seen + 1;
        }
        return Response.ok().build();
    }
}
