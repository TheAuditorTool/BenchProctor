import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PlaceOrder } from "./order_submit";
import { LoadPolicy } from "./load_policy";
import { AuditRoster } from "./audit_roster";
import { RenderProfile } from "./render_profile";
import { RotateWindow } from "./rotate_window";
import { CompactPolicy } from "./compact_policy";
import { BuildCheckpoint } from "./build_checkpoint";
import { VerifyPromotion } from "./verify_promotion";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PlaceOrder, LoadPolicy, AuditRoster, RenderProfile, RotateWindow, CompactPolicy, BuildCheckpoint, VerifyPromotion],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
