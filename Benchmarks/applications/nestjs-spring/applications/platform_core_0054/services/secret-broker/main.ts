import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { FetchSecret } from "./secret_fetch";
import { BuildReceipt } from "./build_receipt";
import { RotateSummary } from "./rotate_summary";
import { CompactSecret } from "./compact_secret";
import { RotateConfig } from "./rotate_config";
import { PublishSecret } from "./publish_secret";
import { ReconcileThreshold } from "./reconcile_threshold";
import { MergeRecord } from "./merge_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, FetchSecret, BuildReceipt, RotateSummary, CompactSecret, RotateConfig, PublishSecret, ReconcileThreshold, MergeRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
