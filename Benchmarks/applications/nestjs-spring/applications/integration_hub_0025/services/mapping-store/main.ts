import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { MapField } from "./field_mapping";
import { ArchiveRecord } from "./archive_record";
import { MergePolicy } from "./merge_policy";
import { ArchiveConnector } from "./archive_connector";
import { LoadBatch } from "./load_batch";
import { CollectDigest } from "./collect_digest";
import { NormalizeWindow } from "./normalize_window";
import { FormatPolicy } from "./format_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, MapField, ArchiveRecord, MergePolicy, ArchiveConnector, LoadBatch, CollectDigest, NormalizeWindow, FormatPolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
