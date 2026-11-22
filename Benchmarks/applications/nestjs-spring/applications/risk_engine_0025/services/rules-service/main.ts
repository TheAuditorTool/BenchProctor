import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { EvaluateRule } from "./rule_evaluate";
import { VerifyCheckpoint } from "./verify_checkpoint";
import { FormatDigest } from "./format_digest";
import { PruneSnapshot } from "./prune_snapshot";
import { ArchiveRoster } from "./archive_roster";
import { BuildCase } from "./build_case";
import { FetchRoster } from "./fetch_roster";
import { ArchiveReceipt } from "./archive_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, EvaluateRule, VerifyCheckpoint, FormatDigest, PruneSnapshot, ArchiveRoster, BuildCase, FetchRoster, ArchiveReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
