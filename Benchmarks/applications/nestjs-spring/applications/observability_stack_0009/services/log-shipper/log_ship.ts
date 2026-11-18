// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("log-shipper")
export class ShipLog {
  @Post("shipLog")
  async shipLog(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const gauge = Buffer.from(summary, "hex").toString();
    await fetch("http://anomaly-scorer:8080/ScoreAnomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
