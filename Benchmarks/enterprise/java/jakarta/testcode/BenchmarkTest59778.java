// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.xpath.*;

@Path("/")
public class BenchmarkTest59778 {

    @GET
    @Path("/BenchmarkTest59778")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59778(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "" + hostValue;
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
