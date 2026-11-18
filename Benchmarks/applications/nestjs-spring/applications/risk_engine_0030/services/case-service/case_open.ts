// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class OpenCase {
  @Post("openCase")
  async openCase(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const grievance = tokens.join(' ');
    await fetch("http://alert-triage:8080/TriageAlert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
    return { created: true };
  }
}
