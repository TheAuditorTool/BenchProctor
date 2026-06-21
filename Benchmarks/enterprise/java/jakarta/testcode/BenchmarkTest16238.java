// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest16238 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GET
    @Path("/BenchmarkTest16238")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16238(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = expandTabs(hostValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
