// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("knowledge-index")
export class RenderTicket {
  @Post("renderTicket")
  async renderTicket(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const _raw = remark;
    const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", inquiry);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const grievance = resolved;
    const fileContent = fs.readFileSync(grievance, "utf8");
    return fileContent;
  }
}
