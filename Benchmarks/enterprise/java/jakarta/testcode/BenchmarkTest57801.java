// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest57801 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GET
    @Path("/BenchmarkTest57801/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest57801(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = collapseWhitespace(pathValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
