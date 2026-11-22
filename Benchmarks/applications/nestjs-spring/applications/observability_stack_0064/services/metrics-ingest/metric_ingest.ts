// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("metrics-ingest")
export class IngestMetric {
  @Post("ingestMetric")
  @UseGuards(AuthGuard)
  async ingestMetric(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body.payload as string) || "";
    const gauge = `${tagline}`;
    await fetch("http://dashboard-api:8080/QueryDashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
