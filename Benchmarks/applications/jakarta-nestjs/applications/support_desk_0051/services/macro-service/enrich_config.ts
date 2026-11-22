// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("macro-service")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const _raw = preface;
    const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", grievance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const inquiry = resolved;
    const fileContent = fs.readFileSync(inquiry, "utf8");
    return fileContent;
  }
}
