// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("redaction-service")
export class NormalizeReport {
  @Post("normalizeReport")
  async normalizeReport(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    const _raw = phrase;
    const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", dossier);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const addendum = resolved;
    const fileContent = fs.readFileSync(addendum, "utf8");
    return fileContent;
  }
}
