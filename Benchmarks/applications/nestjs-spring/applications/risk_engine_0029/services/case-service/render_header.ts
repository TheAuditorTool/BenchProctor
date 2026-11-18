// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("case-service")
export class RenderHeader {
  @Post("renderHeader")
  async renderHeader(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(subject);
    const resolved = path.resolve("/var/app/data", grievance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const verdict = resolved;
    fs.writeFileSync(verdict, "data");
    return { created: true };
  }
}
