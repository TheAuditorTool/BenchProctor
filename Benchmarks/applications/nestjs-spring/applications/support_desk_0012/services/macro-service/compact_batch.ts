// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("macro-service")
export class CompactBatch {
  @Post("compactBatch")
  async compactBatch(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const grievance = tokens.join(' ');
    return "<div>" + grievance + "</div>";
  }
}
