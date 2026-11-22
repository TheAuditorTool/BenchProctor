import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterMandate } from "./mandate_register";
import { EnrichRoster } from "./enrich_roster";
import { VerifyBatch } from "./verify_batch";
import { VerifyRoster } from "./verify_roster";
import { MergeReport } from "./merge_report";
import { CompactConfig } from "./compact_config";
import { MergeThreshold } from "./merge_threshold";
import { ArchiveSnapshot } from "./archive_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterMandate, EnrichRoster, VerifyBatch, VerifyRoster, MergeReport, CompactConfig, MergeThreshold, ArchiveSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
