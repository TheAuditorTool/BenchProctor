import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { OpenCase } from "./case_open";
import { SummarizeConfig } from "./summarize_config";
import { RotateProfile } from "./rotate_profile";
import { FetchWindow } from "./fetch_window";
import { ArchiveLedger } from "./archive_ledger";
import { PruneSummary } from "./prune_summary";
import { RenderHeader } from "./render_header";
import { CompactDigest } from "./compact_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, OpenCase, SummarizeConfig, RotateProfile, FetchWindow, ArchiveLedger, PruneSummary, RenderHeader, CompactDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
