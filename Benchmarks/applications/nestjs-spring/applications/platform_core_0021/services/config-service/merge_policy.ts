// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("config-service")
export class MergePolicy {
  @Post("mergePolicy")
  async mergePolicy(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(excerpt);
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const persona = resolved;
    fs.writeFileSync(persona, "data");
    return { created: true };
  }
}
