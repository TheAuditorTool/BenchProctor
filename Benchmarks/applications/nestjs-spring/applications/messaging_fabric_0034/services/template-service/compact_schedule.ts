// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("template-service")
export class CompactSchedule {
  @Post("compactSchedule")
  async compactSchedule(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    return "<div>" + bulletin + "</div>";
  }
}
