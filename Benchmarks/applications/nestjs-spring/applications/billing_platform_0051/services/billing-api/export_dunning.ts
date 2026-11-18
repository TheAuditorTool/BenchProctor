// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("billing-api")
export class ExportDunning {
  @Post("exportDunning")
  async exportDunning(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const arrears: string = transform(synopsis);
    const resolved = path.resolve("/var/app/data", arrears);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dunning = resolved;
    fs.writeFileSync(dunning, "data");
    return { created: true };
  }
}
