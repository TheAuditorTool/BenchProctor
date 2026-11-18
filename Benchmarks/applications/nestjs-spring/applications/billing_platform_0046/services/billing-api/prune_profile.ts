// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("billing-api")
export class PruneProfile {
  @Post("pruneProfile")
  async pruneProfile(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(remittance)) { throw new ForbiddenException({error:"forbidden"}); }
    const arrears = "/var/app/data/" + remittance;
    fs.unlinkSync(arrears);
    return { created: true };
  }
}
