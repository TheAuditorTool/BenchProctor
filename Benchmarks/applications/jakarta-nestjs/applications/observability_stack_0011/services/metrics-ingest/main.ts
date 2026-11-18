import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { IngestMetric } from "./metric_ingest";
import { SummarizeTrace } from "./summarize_trace";
import { FormatHeader } from "./format_header";
import { NormalizeConfig } from "./normalize_config";
import { SummarizeDigest } from "./summarize_digest";
import { PublishCheckpoint } from "./publish_checkpoint";
import { ExportDigest } from "./export_digest";
import { NormalizeIndex } from "./normalize_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IngestMetric, SummarizeTrace, FormatHeader, NormalizeConfig, SummarizeDigest, PublishCheckpoint, ExportDigest, NormalizeIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
