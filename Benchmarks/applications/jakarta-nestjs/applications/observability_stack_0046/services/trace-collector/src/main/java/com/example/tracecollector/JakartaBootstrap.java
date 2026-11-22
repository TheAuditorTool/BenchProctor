package com.example.tracecollector;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.tracecollector.JakartaBootstrap$HealthResource,com.example.tracecollector.CollectMetric,com.example.tracecollector.CollectTrace,com.example.tracecollector.CompactSchedule,com.example.tracecollector.FetchReport,com.example.tracecollector.FormatProfile,com.example.tracecollector.PruneDigest,com.example.tracecollector.PruneProfile,com.example.tracecollector.SummarizeRoster");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
