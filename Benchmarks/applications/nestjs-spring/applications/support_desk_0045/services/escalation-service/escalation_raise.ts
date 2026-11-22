// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class RaiseEscalation {
  @Post("raiseEscalation")
  async raiseEscalation(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.payload as string) || "";
    const [inquiry] = String(remark).split(',');
    await fetch("http://knowledge-index:8080/SearchKnowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
