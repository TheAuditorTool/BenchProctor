import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AuthorizePayment } from "./payment_authorize";
import { PublishPayout } from "./publish_payout";
import { AuditSnapshot } from "./audit_snapshot";
import { MergeBatch } from "./merge_batch";
import { MergeReceipt } from "./merge_receipt";
import { RotateThreshold } from "./rotate_threshold";
import { LoadRecord } from "./load_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AuthorizePayment, PublishPayout, AuditSnapshot, MergeBatch, MergeReceipt, RotateThreshold, LoadRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
