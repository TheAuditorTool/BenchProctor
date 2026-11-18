// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("supplier-feed")
export class SummarizeAllocation {
  @Post("summarizeAllocation")
  async summarizeAllocation(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const restock = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(restock)) { throw new ForbiddenException({error:"forbidden"}); }
    const backorder = "/var/app/data/" + restock;
    fs.unlinkSync(backorder);
    return { created: true };
  }
}
