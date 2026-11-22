// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class RaiseEscalation {
  @Post("raiseEscalation")
  async raiseEscalation(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.host as string) || "";
    const grievance = `${preface}`;
    await fetch("http://macro-service:8080/ApplyMacro", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
    return { created: true };
  }
}
