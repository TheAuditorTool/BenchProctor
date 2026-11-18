// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("retention-service")
export class SweepRetention {
  @Post("sweepRetention")
  async sweepRetention(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const cohort = Buffer.from(headline, "base64").toString();
    await fetch("http://dashboard-api:8080/QueryDashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
