// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("dispute-service")
export class FormatWindow {
  @Post("formatWindow")
  async formatWindow(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers.origin as string) || "";
    const pending: string[] = String(passage).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const remittance: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", remittance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const disbursement = resolved;
    fs.writeFileSync(disbursement, "data");
    return { created: true };
  }
}
