// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    const consignment = parcel.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + consignment + "</div>";
  }
}
