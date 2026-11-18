// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ticket-router")
export class ReconcileCheckpoint {
  @Post("reconcileCheckpoint")
  async reconcileCheckpoint(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    return "<div>" + inquiry + "</div>";
  }
}
