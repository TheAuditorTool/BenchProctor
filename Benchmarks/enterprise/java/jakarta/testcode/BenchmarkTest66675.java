// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest66675 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GET
    @Path("/BenchmarkTest66675")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest66675(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = collapseWhitespace(uaValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        new java.io.File("/tmp/" + processed).createNewFile();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
