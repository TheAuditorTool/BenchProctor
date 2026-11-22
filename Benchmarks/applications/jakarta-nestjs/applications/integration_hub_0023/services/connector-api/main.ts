import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { InvokeConnector } from "./connector_invoke";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { VerifyThreshold } from "./verify_threshold";
import { MergeReceipt } from "./merge_receipt";
import { LoadPartner } from "./load_partner";
import { RenderRoster } from "./render_roster";
import { VerifyManifest } from "./verify_manifest";
import { LoadSummary } from "./load_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InvokeConnector, ReconcileSnapshot, VerifyThreshold, MergeReceipt, LoadPartner, RenderRoster, VerifyManifest, LoadSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
