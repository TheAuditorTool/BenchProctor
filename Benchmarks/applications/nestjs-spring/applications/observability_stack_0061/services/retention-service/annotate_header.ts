// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("retention-service")
export class AnnotateHeader {
  @Post("annotateHeader")
  async annotateHeader(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(headline);
    const resolved = path.resolve("/var/app/data", cohort);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const gauge = resolved;
    fs.writeFileSync(gauge, "data");
    return { created: true };
  }
}
