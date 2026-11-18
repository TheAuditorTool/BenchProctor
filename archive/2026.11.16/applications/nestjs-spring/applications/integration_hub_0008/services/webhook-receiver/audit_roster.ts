// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("webhook-receiver")
export class AuditRoster {
  @Post("auditRoster")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    const tokens = String(preface).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    const paragraph = handshake.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + paragraph + "</div>";
  }
}
