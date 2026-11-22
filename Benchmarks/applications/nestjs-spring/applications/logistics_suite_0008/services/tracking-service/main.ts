import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { PollTracking } from "./tracking_poll";
import { ArchiveReport } from "./archive_report";
import { EnrichWindow } from "./enrich_window";
import { LoadSchedule } from "./load_schedule";
import { PruneSummary } from "./prune_summary";
import { FetchLedger } from "./fetch_ledger";
import { ExportBundle } from "./export_bundle";
import { LoadDigest } from "./load_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PollTracking, ArchiveReport, EnrichWindow, LoadSchedule, PruneSummary, FetchLedger, ExportBundle, LoadDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
