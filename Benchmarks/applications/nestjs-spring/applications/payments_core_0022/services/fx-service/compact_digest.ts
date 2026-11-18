// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("fx-service")
export class CompactDigest {
  @Post("compactDigest")
  async compactDigest(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const tokens = String(subject).split(',').filter((t) => t.length > 0);
    const ledger = tokens.join(' ');
    return "<div>" + ledger + "</div>";
  }
}
