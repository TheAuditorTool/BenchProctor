// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest48881 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @POST
    @Path("/BenchmarkTest48881")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48881(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripCRLF(xmlValue);
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
