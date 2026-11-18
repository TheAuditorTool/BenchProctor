// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("customs-service")
export class ExportSummary {
  @Post("exportSummary")
  async exportSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.origin as string) || "";
    const pending: string[] = String(footnote).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const parcel: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", parcel);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const consignment = resolved;
    fs.writeFileSync(consignment, "data");
    return { created: true };
  }
}
