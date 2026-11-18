// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("catalog-api")
export class SummarizeBatch {
  @Post("summarizeBatch")
  async summarizeBatch(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.origin as string) || "";
    const pending: string[] = String(phrase).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const backorder: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", backorder);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const restock = resolved;
    fs.writeFileSync(restock, "data");
    return { created: true };
  }
}
