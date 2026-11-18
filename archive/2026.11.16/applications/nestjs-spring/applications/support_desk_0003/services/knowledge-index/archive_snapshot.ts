// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("knowledge-index")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.origin as string) || "";
    const pending: string[] = String(citation).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const grievance: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", grievance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const inquiry = resolved;
    fs.writeFileSync(inquiry, "data");
    return { created: true };
  }
}
