// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("message-api")
export class LoadLedger {
  @Post("loadLedger")
  async loadLedger(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    const notice = bulletin.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + notice + "</div>";
  }
}
