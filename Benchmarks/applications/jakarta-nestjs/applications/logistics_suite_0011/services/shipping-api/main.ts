import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QuoteShipment } from "./shipment_quote";
import { AuditRoster } from "./audit_roster";
import { RotateHeader } from "./rotate_header";
import { NormalizeWindow } from "./normalize_window";
import { RotateSnapshot } from "./rotate_snapshot";
import { CollectManifest } from "./collect_manifest";
import { PruneProfile } from "./prune_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, AuditRoster, RotateHeader, NormalizeWindow, RotateSnapshot, CollectManifest, PruneProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
