// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("partner-registry")
export class RotateDigest {
  @Post("rotateDigest")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.origin as string) || "";
    const pending: string[] = String(quotation).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const handshake: string = collected.join(',');
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const preface = resolved;
    fs.writeFileSync(preface, "data");
    return { created: true };
  }
}
