import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PullSupplierFeed } from "./supplier_feed";
import { ExportRecord } from "./export_record";
import { FormatBundle } from "./format_bundle";
import { ExportSnapshot } from "./export_snapshot";
import { PublishCheckpoint } from "./publish_checkpoint";
import { PublishDigest } from "./publish_digest";
import { ReconcileBatch } from "./reconcile_batch";
import { CompactCheckpoint } from "./compact_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PullSupplierFeed, ExportRecord, FormatBundle, ExportSnapshot, PublishCheckpoint, PublishDigest, ReconcileBatch, CompactCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
