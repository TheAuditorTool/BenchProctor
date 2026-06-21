// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest82636 {

    @GET
    @Path("/BenchmarkTest82636")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82636(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", uaValue);
        String data = sw.toString();
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
