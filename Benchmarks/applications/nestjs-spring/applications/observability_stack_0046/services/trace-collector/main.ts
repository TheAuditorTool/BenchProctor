import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { CollectTrace } from "./trace_collect";
import { FetchReport } from "./fetch_report";
import { PruneDigest } from "./prune_digest";
import { CompactSchedule } from "./compact_schedule";
import { FormatProfile } from "./format_profile";
import { CollectMetric } from "./collect_metric";
import { PruneProfile } from "./prune_profile";
import { SummarizeRoster } from "./summarize_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CollectTrace, FetchReport, PruneDigest, CompactSchedule, FormatProfile, CollectMetric, PruneProfile, SummarizeRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
