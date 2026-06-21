// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25137 {

    @POST
    @Path("/BenchmarkTest25137")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25137(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        byte[] raw = rawData.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
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
