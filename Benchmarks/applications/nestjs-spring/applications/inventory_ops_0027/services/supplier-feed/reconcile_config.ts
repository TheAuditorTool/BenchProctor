// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("supplier-feed")
export class ReconcileConfig {
  @Post("reconcileConfig")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const restock: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(restock)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = restock;
    return "<div>" + backorder + "</div>";
  }
}
