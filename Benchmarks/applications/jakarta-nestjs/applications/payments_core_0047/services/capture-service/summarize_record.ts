// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("capture-service")
export class SummarizeRecord {
  @Post("summarizeRecord")
  async summarizeRecord(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    const _raw = footnote;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", remittance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const disbursement = resolved;
    const fileContent = fs.readFileSync(disbursement, "utf8");
    return fileContent;
  }
}
