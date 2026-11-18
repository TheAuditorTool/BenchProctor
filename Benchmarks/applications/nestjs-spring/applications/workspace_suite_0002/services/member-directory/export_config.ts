// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("member-directory")
export class ExportConfig {
  @Post("exportConfig")
  async exportConfig(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const heading: string = transform(transcript);
    const resolved = path.resolve("/var/app/data", heading);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const passage = resolved;
    fs.writeFileSync(passage, "data");
    return { created: true };
  }
}
