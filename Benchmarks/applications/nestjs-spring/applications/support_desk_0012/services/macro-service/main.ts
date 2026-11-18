import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyMacro } from "./macro_apply";
import { CompactBatch } from "./compact_batch";
import { LoadConfig } from "./load_config";
import { NormalizeRoster } from "./normalize_roster";
import { MergeSummary } from "./merge_summary";
import { ExportPolicy } from "./export_policy";
import { AnnotateReport } from "./annotate_report";
import { FetchDigest } from "./fetch_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyMacro, CompactBatch, LoadConfig, NormalizeRoster, MergeSummary, ExportPolicy, AnnotateReport, FetchDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
