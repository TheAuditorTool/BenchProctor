import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AcceptWebhook } from "./webhook_accept";
import { ReconcileBatch } from "./reconcile_batch";
import { EnrichLedger } from "./enrich_ledger";
import { AuditRoster } from "./audit_roster";
import { VerifyPartner } from "./verify_partner";
import { EnrichWebhook } from "./enrich_webhook";
import { ReconcileSchedule } from "./reconcile_schedule";
import { PublishThreshold } from "./publish_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AcceptWebhook, ReconcileBatch, EnrichLedger, AuditRoster, VerifyPartner, EnrichWebhook, ReconcileSchedule, PublishThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
