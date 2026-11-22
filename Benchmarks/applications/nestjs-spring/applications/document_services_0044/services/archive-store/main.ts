import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { StoreArchive } from "./archive_store";
import { SummarizeConfig } from "./summarize_config";
import { CompactIndex } from "./compact_index";
import { ArchiveSchedule } from "./archive_schedule";
import { FormatRedaction } from "./format_redaction";
import { ArchiveBundle } from "./archive_bundle";
import { VerifyPolicy } from "./verify_policy";
import { ReconcilePolicy } from "./reconcile_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreArchive, SummarizeConfig, CompactIndex, ArchiveSchedule, FormatRedaction, ArchiveBundle, VerifyPolicy, ReconcilePolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
