// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ticket-router")
export class AuditSummary {
  @Post("auditSummary")
  async auditSummary(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    const grievance = inquiry.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + grievance + "</div>";
  }
}
