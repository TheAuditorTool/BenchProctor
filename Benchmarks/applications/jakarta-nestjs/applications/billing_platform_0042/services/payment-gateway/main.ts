import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CapturePayment } from "./payment_capture";
import { RenderBatch } from "./render_batch";
import { BuildSummary } from "./build_summary";
import { RenderSnapshot } from "./render_snapshot";
import { AnnotatePolicy } from "./annotate_policy";
import { RenderInvoice } from "./render_invoice";
import { BuildLedger } from "./build_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CapturePayment, RenderBatch, BuildSummary, RenderSnapshot, AnnotatePolicy, RenderInvoice, BuildLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
