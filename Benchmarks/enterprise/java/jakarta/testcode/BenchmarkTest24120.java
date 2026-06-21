// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.xpath.*;

@Path("/")
public class BenchmarkTest24120 {

    @GET
    @Path("/BenchmarkTest24120/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest24120(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + pathValue + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
