import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ConfigureSample } from "./sample_config";
import { FetchConfig } from "./fetch_config";
import { AnnotateReport } from "./annotate_report";
import { EnrichReceipt } from "./enrich_receipt";
import { MergeReceipt } from "./merge_receipt";
import { RenderManifest } from "./render_manifest";
import { CompactBatch } from "./compact_batch";
import { LoadBatch } from "./load_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConfigureSample, FetchConfig, AnnotateReport, EnrichReceipt, MergeReceipt, RenderManifest, CompactBatch, LoadBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
