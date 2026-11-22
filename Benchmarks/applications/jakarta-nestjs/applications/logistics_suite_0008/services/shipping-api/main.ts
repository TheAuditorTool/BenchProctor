import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { QuoteShipment } from "./shipment_quote";
import { PublishLedger } from "./publish_ledger";
import { VerifyThreshold } from "./verify_threshold";
import { FetchPolicy } from "./fetch_policy";
import { FormatReport } from "./format_report";
import { MergeBatch } from "./merge_batch";
import { BuildSnapshot } from "./build_snapshot";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, PublishLedger, VerifyThreshold, FetchPolicy, FormatReport, MergeBatch, BuildSnapshot],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
