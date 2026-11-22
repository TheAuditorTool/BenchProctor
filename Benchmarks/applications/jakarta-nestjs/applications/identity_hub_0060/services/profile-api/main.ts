import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { UpdateProfile } from "./profile_update";
import { FormatSnapshot } from "./format_snapshot";
import { BuildReport } from "./build_report";
import { AuditDevice } from "./audit_device";
import { MergeReceipt } from "./merge_receipt";
import { VerifyWindow } from "./verify_window";
import { NormalizeProfile } from "./normalize_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdateProfile, FormatSnapshot, BuildReport, AuditDevice, MergeReceipt, VerifyWindow, NormalizeProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
