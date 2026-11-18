// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("dispute-service")
export class MergeIndex {
  @Post("mergeIndex")
  async mergeIndex(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.origin as string) || "";
    const pending: string[] = String(subtitle).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const ledger: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", ledger);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const remittance = resolved;
    fs.writeFileSync(remittance, "data");
    return { created: true };
  }
}
