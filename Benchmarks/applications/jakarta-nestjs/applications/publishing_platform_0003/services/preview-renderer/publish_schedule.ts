// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("preview-renderer")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const heading = (req.cookies?.session_token as string) || "";
    const _raw = heading;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", addendum);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const byline = resolved;
    const fileContent = fs.readFileSync(byline, "utf8");
    return fileContent;
  }
}
