import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { ConfigureSample } from "./sample_config";
import { SummarizeSchedule } from "./summarize_schedule";
import { MergeDigest } from "./merge_digest";
import { ArchiveManifest } from "./archive_manifest";
import { PruneRecord } from "./prune_record";
import { CompactMetric } from "./compact_metric";
import { FormatRoster } from "./format_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConfigureSample, SummarizeSchedule, MergeDigest, ArchiveManifest, PruneRecord, CompactMetric, FormatRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
