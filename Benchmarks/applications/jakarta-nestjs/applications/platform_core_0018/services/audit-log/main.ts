import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { AppendAudit } from "./audit_append";
import { RenderSecret } from "./render_secret";
import { ValidateTenant } from "./validate_tenant";
import { NormalizeFlag } from "./normalize_flag";
import { ArchiveCheckpoint } from "./archive_checkpoint";
import { ValidatePolicy } from "./validate_policy";
import { FetchRoster } from "./fetch_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AppendAudit, RenderSecret, ValidateTenant, NormalizeFlag, ArchiveCheckpoint, ValidatePolicy, FetchRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
