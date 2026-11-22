import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DispatchCarrier } from "./carrier_dispatch";
import { FetchProfile } from "./fetch_profile";
import { AuditShipment } from "./audit_shipment";
import { VerifyCarrier } from "./verify_carrier";
import { RotateLabel } from "./rotate_label";
import { EnrichRoster } from "./enrich_roster";
import { CollectLabel } from "./collect_label";
import { ValidatePolicy } from "./validate_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchCarrier, FetchProfile, AuditShipment, VerifyCarrier, RotateLabel, EnrichRoster, CollectLabel, ValidatePolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
