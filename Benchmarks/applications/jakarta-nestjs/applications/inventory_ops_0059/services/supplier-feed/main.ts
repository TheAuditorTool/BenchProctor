import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { PullSupplierFeed } from "./supplier_feed";
import { ArchiveSnapshot } from "./archive_snapshot";
import { PruneHeader } from "./prune_header";
import { ValidateWindow } from "./validate_window";
import { FetchLedger } from "./fetch_ledger";
import { VerifyDigest } from "./verify_digest";
import { ResolveSnapshot } from "./resolve_snapshot";
import { FormatPolicy } from "./format_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PullSupplierFeed, ArchiveSnapshot, PruneHeader, ValidateWindow, FetchLedger, VerifyDigest, ResolveSnapshot, FormatPolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
