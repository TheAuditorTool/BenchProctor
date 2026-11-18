import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { IndexMetadata } from "./metadata_index";
import { ReconcileRecord } from "./reconcile_record";
import { FetchReceipt } from "./fetch_receipt";
import { FormatReport } from "./format_report";
import { FetchBatch } from "./fetch_batch";
import { FormatPolicy } from "./format_policy";
import { ValidateBundle } from "./validate_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexMetadata, ReconcileRecord, FetchReceipt, FormatReport, FetchBatch, FormatPolicy, ValidateBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
