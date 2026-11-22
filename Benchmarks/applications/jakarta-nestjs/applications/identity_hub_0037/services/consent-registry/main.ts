import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RecordConsent } from "./consent_record";
import { MergePolicy } from "./merge_policy";
import { LoadPolicy } from "./load_policy";
import { ValidateLedger } from "./validate_ledger";
import { BuildWindow } from "./build_window";
import { ArchiveReceipt } from "./archive_receipt";
import { RotateSummary } from "./rotate_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RecordConsent, MergePolicy, LoadPolicy, ValidateLedger, BuildWindow, ArchiveReceipt, RotateSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
