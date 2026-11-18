// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("macro-service")
export class ApplyMacro {
  @Post("applyMacro")
  async applyMacro(@Req() req: Request): Promise<unknown> {
    const summary = process.env.SUPPORT_INPUT_0012 || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    await fetch("http://escalation-service:8080/RaiseEscalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
    return { created: true };
  }
}
