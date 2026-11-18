// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("share-service")
export class LoadSummary {
  @Post("loadSummary")
  async loadSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.origin as string) || "";
    const pending: string[] = String(summary).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const subtitle: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", subtitle);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const notice = resolved;
    fs.writeFileSync(notice, "data");
    return { created: true };
  }
}
