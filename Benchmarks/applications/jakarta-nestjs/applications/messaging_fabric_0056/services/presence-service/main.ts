import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { UpdatePresence } from "./presence_update";
import { FormatHeader } from "./format_header";
import { CollectBundle } from "./collect_bundle";
import { MergeLedger } from "./merge_ledger";
import { LoadMessage } from "./load_message";
import { VerifyHeader } from "./verify_header";
import { LoadRecord } from "./load_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdatePresence, FormatHeader, CollectBundle, MergeLedger, LoadMessage, VerifyHeader, LoadRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
