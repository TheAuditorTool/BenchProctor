import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ConvertFx } from "./fx_convert";
import { CompactReceipt } from "./compact_receipt";
import { MergeSnapshot } from "./merge_snapshot";
import { NormalizeDispute } from "./normalize_dispute";
import { ReconcileConfig } from "./reconcile_config";
import { FormatPolicy } from "./format_policy";
import { ValidateReceipt } from "./validate_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConvertFx, CompactReceipt, MergeSnapshot, NormalizeDispute, ReconcileConfig, FormatPolicy, ValidateReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
