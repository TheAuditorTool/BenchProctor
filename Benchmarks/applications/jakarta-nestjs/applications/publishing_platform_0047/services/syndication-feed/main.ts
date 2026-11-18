import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PushSyndication } from "./syndication_push";
import { EnrichSummary } from "./enrich_summary";
import { ExportConfig } from "./export_config";
import { FetchTaxonomy } from "./fetch_taxonomy";
import { CompactRoster } from "./compact_roster";
import { MergeHeader } from "./merge_header";
import { CompactRevision } from "./compact_revision";
import { EnrichThreshold } from "./enrich_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PushSyndication, EnrichSummary, ExportConfig, FetchTaxonomy, CompactRoster, MergeHeader, CompactRevision, EnrichThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
