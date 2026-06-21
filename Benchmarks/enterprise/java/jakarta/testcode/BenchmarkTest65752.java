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
public class BenchmarkTest65752 {

    private static String normalize(String v) { return v.strip(); }

    @POST
    @Path("/BenchmarkTest65752")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65752(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        new java.io.File("/tmp/" + data).createNewFile();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
