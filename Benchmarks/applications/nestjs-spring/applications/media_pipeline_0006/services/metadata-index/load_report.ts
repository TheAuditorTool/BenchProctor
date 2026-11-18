// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("metadata-index")
export class LoadReport {
  @Post("loadReport")
  async loadReport(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const montage: string = transform(passage);
    const resolved = path.resolve("/var/app/data", montage);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const rendition = resolved;
    fs.writeFileSync(rendition, "data");
    return { created: true };
  }
}
