// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("session-store")
export class ValidateManifest {
  @Post("validateManifest")
  async validateManifest(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.origin as string) || "";
    const pending: string[] = String(excerpt).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const wording = resolved;
    fs.writeFileSync(wording, "data");
    return { created: true };
  }
}
