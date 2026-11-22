// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("sla-monitor")
export class CheckSla {
  @Post("checkSla")
  async checkSla(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(preface);
    await fetch("http://escalation-service:8080/RaiseEscalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
    return { created: true };
  }
}
