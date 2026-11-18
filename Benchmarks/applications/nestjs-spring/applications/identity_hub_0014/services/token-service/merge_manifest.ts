// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("token-service")
export class MergeManifest {
  @Post("mergeManifest")
  async mergeManifest(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(snippet);
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const synopsis = resolved;
    fs.writeFileSync(synopsis, "data");
    return { created: true };
  }
}
