// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dashboard-api")
export class QueryDashboard {
  @Post("queryDashboard")
  async queryDashboard(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(summary);
    await fetch("http://retention-service:8080/SweepRetention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
    return { created: true };
  }
}
