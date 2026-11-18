// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("anomaly-scorer")
export class ScoreAnomaly {
  @Post("scoreAnomaly")
  async scoreAnomaly(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.host as string) || "";
    const gauge = `${excerpt}`;
    await fetch("http://alert-router:8080/RouteAlert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
    return { created: true };
  }
}
